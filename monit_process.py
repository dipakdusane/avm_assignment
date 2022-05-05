
import psutil
import os
import sys


def send_mail(process_name, email_msg_line=None):
	fromaddr = "dipak.dusane@gmail.com"
	toaddrs  = "dipak.dusane@gmail.com"
	msg = ("From: %s To: %s" % (fromaddr, toaddrs))
	if email_msg_line is None:
		email_msg_line = "process has stopped {}".format(process_name)
	msg = msg + email_msg_line
	server = smtplib.SMTP('localhost')
	server.set_debuglevel(1)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()


def monitor_process(process_name):
	threshold_cpu = 50.0
	for proc in psutil.process_iter(['pid', 'name', 'username']):
		if proc.name().lower() == process_name.lower(): 
			if proc.is_running():
				print(proc.pid, proc.name)
			elif proc.is_running() and proc.cpu_percent() > threshold_cpu
				current_cpu = proc.cpu_percent()
				custom_msg = "Process consuming more than threshold_cpu %s" % (str(current_cpu))
				send_mail(process_name, email_msg_line=custom_msg)
			else:
				send_mail(process_name)


if __name__ == "__main__":
	process_name = "MusicCacheExtension"
	monitor_process(process_name)