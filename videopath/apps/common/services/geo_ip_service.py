import pygeoip
import os

def record_by_address(ip):
	dat_path = os.path.dirname(os.path.abspath(__file__)) + "/assets/GeoIP.dat"
	try:
	    gi = pygeoip.GeoIP(dat_path, pygeoip.MEMORY_CACHE)
	    country = gi.country_code_by_addr(ip)
	    continent = pygeoip.const.COUNTRY_CODES.index(country)
	    continent = pygeoip.const.CONTINENT_NAMES[pygeoip.const.COUNTRY_CODES.index(country)]
	    return {
	    	"continent": continent,
	    	"country": country
	    }
	except:
	    return {
	    	"continent": "--",
	    	"country": "--"
	    }


def record_from_request(request):
	# get correct ip
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
	    ip = x_forwarded_for.split(',')[0]
	else:
	    ip = request.META.get('REMOTE_ADDR')
	return record_by_address(ip)

