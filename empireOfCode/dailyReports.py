import datetime
import re


count_ingots=lambda r: sum([(ord(x[0])-65)*9+int(x[1])for x in r.split(',')])

def count_reports(full_report, from_date, to_date):
    dFrom = datetime.datetime.strptime(from_date, "%Y-%m-%d")
    dTo = datetime.datetime.strptime(to_date, "%Y-%m-%d")
    reports = re.findall('\d{4}-\d{2}-\d{2} .*', full_report)
    x = [ count_ingots(report.split()[1]) for report in reports if dFrom <=  datetime.datetime.strptime(report.split()[0], "%Y-%m-%d") <= dTo]
    return sum(x)
    """
    for report in reports:
        d,r = report.split()
        d = datetime.datetime.strptime(d, "%Y-%m-%d")
        print "la", d,r
        if dFrom <= d <= dTo:
            print "fit", r
            total += count_ingots(r)
    #print "ici", d

    #for line in full_report.split():
    #    print line

    print total
    """
    return total


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_reports("2015-01-01 A1,B2\n"
                         "2015-01-05 C3,C2,C1\n"
                         "2015-02-01 B4\n"
                         "2015-01-03 Z9,Z9",
                         "2015-01-01", "2015-01-31") == 540, "Normal"
    assert count_reports("2000-02-02 Z2,Z1\n"
                         "2000-02-01 Z2,Z1\n"
                         "2000-02-03 Z2,Z1",
                         "2000-02-04", "2000-02-28") == 0, "Zero"
    assert count_reports("2999-12-31 Z9,A1", "2000-01-01", "2999-12-31") == 235, "Millenium"

    print("Earn cool rewards by using the 'Check' button!")
