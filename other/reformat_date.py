def reformatDate(self, date: str) -> str:
    d, m, y = date.split(" ")
    m_dict = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06",
              "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
    return str(y) + "-" + m_dict[m] + "-" + d[:-2].rjust(2, "0")

print(reformatDate(None, "20th Oct 2052"))
print(reformatDate(None, "6th Jun 1933"))