#!/usr/bin/python

from hcpycf import *

password = random_password()
print password

separator()

datestamp = dateStamp()
print datestamp

separator()

mailfrom = "sarasa@hotmail.comaaa"
if ValidateEmail(mailfrom) == 0:
        print "Error on FROM (no valid email?)."
else:
	print "Mail from OK"

separator()

# mailFrom = "email@from"
# mailTo = "email@to"
# mailSubject = "email test"
# mailBody = "email body"
# mySmtp = "mail.domain.com"
# sendEmail(mailFrom, mailTo, mailSubject, mailBody,mySmtp)

separator()

query_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
time.sleep(5)
query_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
diff_time = comp_dates(query_start_time, query_end_time)
print "Start: [" + str(query_start_time) + "]\nEnd: [" + str(query_end_time) + "]\nDiff (seconds): [" + str(diff_time) + "]\n"

cmdStatus,cmdOutput = runCmd("ls -la /")
print cmdStatus
print cmdOutput
