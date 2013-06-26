start: stop serve
	compass watch 

serve:
	nohup python -m SimpleHTTPServer 12345 &

stop:
	python stop.py
	rm -f nohup.out
