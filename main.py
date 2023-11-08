import sys, getopt
from validator import Validator

def main(argv):
    inputUrl = ''
    opts, args = getopt.getopt(argv,"heu:n",["help","url=","errors"])
    validator = Validator()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print ('main.py --url=<url>')
            print ('\t-u, --url\tSet url. ')
            print ('\t-e\tShow all errors. ')
            print ('\t-n\tNumber of how many nodes checks. ')
            sys.exit()
        elif opt in ("-u", "--url"):
            inputUrl = arg
            if len(inputUrl) == 0:
                sys.stderr.write(str("The -u/--url is missing please check and try again. \n"))
            validator.setXml(arg)
        elif opt in ('-e', '--errors'):
            validator.validate()
            for error in validator.errors():
                sys.stderr.write(str(error)+"\n")
            sys.exit()
        elif opt == '-n':
            validator.validate()
            sys.stdout.write(str(validator.checks())+"\n")
            sys.exit()
    
    if inputUrl:
        validator.validate()
        hasErrors = bool(validator.errors())
        return sys.stdout.write(str(not hasErrors)+"\n")

    if len(inputUrl) == 0:
        sys.exit()
        
    
    sys.exit()
if __name__ == "__main__":
    main(sys.argv[1:])