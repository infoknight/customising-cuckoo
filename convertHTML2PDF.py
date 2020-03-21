#!/usr/bin/env python
#pip install html2pdf
#apt-get install wkhtmltopdf


from html2pdf import HTMLToPDF

def main():
    fin = open("report.html","r")
    HTML = fin.readlines()
    h = HTMLToPDF(HTML[0],"report1.pdf")        #Output is saved as /tmp/report1.pdf
    h.render()
    return

if __name__ == "__main__":
    main()
