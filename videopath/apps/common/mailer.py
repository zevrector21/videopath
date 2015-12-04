
from django.template import Context
from django.template.loader import get_template

from videopath.apps.common.services import service_provider

mail_service = service_provider.get_service("mail")

# agents
agents = {
    "ree": {
        "email": "desiree@videopath.com",
        "name": "Desiree dela Rosa"
    }
}


def send_agent_mail(user, subject, template_name, agent, tags):

    if not user.settings.receive_retention_emails:
        return

    # get template
    c = Context({})
    t = get_template("mails/" + template_name + ".txt")
    message = t.render(c)

    agent = agents[agent]
    message = {
        'subject': subject,
        'text': message,
        'to': [{'email': user.email}],
        'from_email': agent["email"],
        'from_name': agent["name"],
        'tags': tags,
    }

    mail_service.mandrill_send(message)


def send_welcome_mail(user):
    send_agent_mail(user, "How's Videopath working?", "welcome", "ree", ['follow up one week'])

def send_follow_up_three_weeks(user):
    send_agent_mail(user, "Get the most out of Videopath", "follow_up_three_weeks", "ree", ['follow up three weeks'])

def send_follow_up_six_weeks(user):
    send_agent_mail(user, "Make Videopath work for you!", "follow_up_six_weeks", "ree", ['follow up six weeks'])

# share mail
def send_share_mail(video, recipients, message):

    try:
        video.current_revision
    except:
        return

    from videopath.apps.files.util.thumbnails_util import thumbnails_for_video

    thumb_url = thumbnails_for_video(video)["large"]
    if not thumb_url.startswith("http"):
        thumb_url = "https:" + thumb_url

    c = Context({
        "thumb_url": thumb_url,
        "user": video.team.owner,
        "message": message,
        "link": "http://player.videopath.com/" + video.key,
        "description": video.current_revision.description,
        "title": video.current_revision.title
    })

    # prepare html version
    t = get_template("mails/share_video.html")
    message_html = t.render(c)

    # prepare plaintext version
    t = get_template("mails/share_video.txt")
    message_plain = t.render(c)

    recipientsmap = []
    for r in recipients:
        recipientsmap.append({'email': r})

    # send
    message = {
        'subject': video.team.owner.username + " shared a video with you!",
        'text': message_plain,
        'html': message_html,
        'to': recipientsmap,
        'from_email': 'no-reply@videopath.com',
        'from_name': 'Videopath Team',
        'tags': ['share'],
        'replyto': video.team.owner.email
    }
    mail_service.mandrill_send(message)

    return True


# regular system mails
def send_mail(user, subject, message_plain, message_html, tags=[], force = False):

    if not force and not user.settings.receive_system_emails:
        return

    message = {
        'subject': subject,
        'text': message_plain,
        'html': message_html,
        'to': [{'email': user.email}],
        'from_email': 'no-reply@videopath.com',
        'from_name': 'Videopath Team',
        'tags': tags,
        'replyto': "support@videopath.com"
    }
    mail_service.mandrill_send(message)


def send_templated_mail(user, subject, template_name, vars, tags, force = False):

    vars["username"] = user.username

    c = Context(vars)

    # prepare html version
    t = get_template("mails/" + template_name + ".html")
    message_html = t.render(c)

    # prepare plaintext version
    t = get_template("mails/" + template_name + ".txt")
    message_plain = t.render(c)

    send_mail(user, subject, message_plain, message_html, tags, force)


### admin  & dev
def send_admin_mail(subject, text):
    from django.contrib.auth.models import User
    users = User.objects.filter(is_superuser=True)
    for user in users:
        send_templated_mail(
            user,
            "Admin Alert: " + subject,
            "admin",
            {"text": text},
            ["admin"]
        )


def send_dev_mail():
    send_templated_mail()

# signup etc.


def send_signup_email(user):
    send_templated_mail(
        user,
        "Hello from Videopath!",
        "signup",
        {},
        ["signup"]
    )


# transcoding mails
def send_transcode_succeeded_mail(source):
    revision = source.revisions.first()
    send_templated_mail(
        revision.video.team.owner,
        "\"" + revision.title + "\" is ready to edit!",
        "transcode_complete",
        {
            "title": revision.title,
            "video_id": revision.video.id
        },
        ["transcode_succeed"]
    )


def send_transcode_failed_mail(source):
    revision = source.revisions.first()

    send_templated_mail(
        revision.video.team.owner,
        "Error processing \"" + revision.title + "\"",
        "transcode_error",
        {
            "title": revision.title
        },
        ["transcode_fail"]
    )


# quota
def send_quota_warning_mail(user):
    send_templated_mail(
        user,
        "You have almost used up your quota this month",
        "quota_warning",
        {},
        ["quota"]
    )


def send_quota_exceeded_mail(user):
    send_templated_mail(
        user,
        "You have exceeded your quota this month",
        "quota_exceeded",
        {},
        ["quota"]
    )

# payment stuff
def send_invoice_created_mail(user, invoice, link):
    send_templated_mail(
        user,
        "Invoice No. " + str(invoice.number),
        "invoice_created",
        {
            "amount_due": invoice.amount_due,
            "link": link,
            "currency": invoice.currency
        },
        ["payment"]
    )

# transcoding jpgs
def send_jpgs_trancode_failed_mail(video):
    send_templated_mail(
        video.team.owner,
        "iPhone Trancoding Failed",
        "jpg_transcode_failed",
        {
            "title": video.draft.title,
        },
        ["jpg_transcoder"]
    )

def send_jpgs_trancode_succeeded_mail(video):
    send_templated_mail(
        video.team.owner,
        "iPhone Trancoding Succeeded",
        "jpg_transcode_succeeded",
        {
            "title": video.draft.title,
        },
        ["jpg_transcoder"]
    )

# subscription emails
def send_subscription_changed_mail(user, plan, interval, is_free):
    send_templated_mail(
        user,
        "Subscription Info",
        "subscribe_change",
        {
            "plan": plan,
            "interval": interval,
            "is_free": is_free
        },
        ["subscription"]
    )


def send_subscription_will_change_mail(user, plan, switch_date):
    send_templated_mail(
        user,
        "Subscription Info",
        "subscribe_will_change",
        {
            "plan": plan,
            "switch_date": switch_date
        },
        ["subscription"]
    )


# forgot pw
def send_forgot_pw_mail(user, password):
    send_templated_mail(
        user,
        "Videopath Password Reset",
        "forgot_password",
        {
            "password": password
        },
        ["forgot_passord"],
        force=True
    )
