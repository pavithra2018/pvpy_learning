"""
1.  Aries         :        Mar 21-Apr 19
2.  Taurus        :        Apr 20-May 20
3.  Gemimi        :        May 21-June 20
4.  Cancer        :        Jun 21-Jul 22
5.  Leo           :        Jul 23-Aug 22
6.  Virgo         :        Aug 23-Sep 22
7.  Libra         :        Sep 23-Oct 22
8.  Scorpio       :        Oct 23-Nov 21
9.  Saggittarius  :        Nov 22-Dec 21
10. Capricon      :        Dec 22-Jan 19
11. Aquiries      :        Jan 20-Feb 18
12. Pisces        :        Feb 19-Mar 20
"""
day = int(input("Input birthday: "))
month = input("Input month of birth :")
if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
elif month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
elif month == 'february':
    astro_sign = 'Aquarius' if (day < 19) else 'pisces'
elif month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'aries'
elif month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'taurus'
elif month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'gemini'
elif month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'cancer'
elif month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'leo'
elif month == 'august':
    astro_sign = 'Leo' if (day < 23) else 'virgo'
elif month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'libra'
elif month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'scorpio'
elif month == 'november':
    astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
print("Your Astrological sign is :",astro_sign)
           
## End   
    