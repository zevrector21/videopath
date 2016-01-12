import conf

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

#
# new mailer implementation
#
def prepare_mail(mailtype, variables, user = None):

    # get config for mail
    mailconf = conf.mails.get(mailtype, {})

    # update some defaults
    fvariables = {
        'to': 'void@videopath.com'
    }

    # default agent
    fvariables.update(conf.agents.get('default'))

    agent = mailconf.get('agent', 'default')

    # set sender
    if agent == 'user' and user:
        fvariables.update({
            "replyto": user.email,
            })
    elif agent != 'user':
        fvariables.update(conf.agents.get(agent))

    if user:
        fvariables.update({
            'to': [{'email':user.email}],
            'username':user.username,
            'user': user
            })


    fvariables.update(variables)
    c = Context(fvariables)

    return {
        'subject': mailconf.get('subject'),
        'text': get_template('mails/{0}.txt'.format(mailtype)).render(c),
        'html': get_template('mails/{0}.html'.format(mailtype)).render(c),
        'tags': [mailtype],
        'from_email': fvariables['from_email'],
        'from_name': fvariables['from_name'],
        'replyto': fvariables['replyto'],
        'to': fvariables['to']
    }

def send_mail(mailtype, variables, user = None):
    conf = prepare_mail(mailtype, variables, user)
    mail_service.mandrill_send(conf)


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
def send_mail_old(user, subject, message_plain, message_html, tags=[], force = False):

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

    send_mail_old(user, subject, message_plain, message_html, tags, force)


### admin & dev
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


