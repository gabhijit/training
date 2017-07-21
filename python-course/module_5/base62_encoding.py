import string
import siphash

key = 'very_top_secret0'

_sip = siphash.SipHash_2_4(key)

all_syms = string.digits + string.lowercase + string.uppercase

def convert_to_base62(num):

    flag = ''
    if num < 0 :
        flag = "-"
        num = num * -1

    outputs = []
    while num > 0:
        output = all_syms[num % 62]
        num /= 62
        outputs.append(output)

    outputs.append(flag)
    outputs = outputs[::-1]
    return ''.join(outputs)

def shorten_url(url):
    shortened_url = 'http://foo.br/'
    if type(url) == int:
        return  convert_to_base62(url)
    elif type(url) == str or type(url) == unicode:
        return convert_to_base62(_sip.update(url).hash())
    else:
        return None

if __name__ == '__main__':
    long_url = 'http://www.google.com/rather_very_long_url'
    print len(long_url)
    shortened_url = 'http://bit.ly/'
    shortened_url = shortened_url + convert_to_base62(_sip.update('http://www.google.com/aratherverywrongurl').hash())
    print shortened_url, len(shortened_url)
