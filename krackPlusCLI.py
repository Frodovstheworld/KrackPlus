import optparse
import subprocess

def main():
    parse = optparse.OptionParser();
    
    #Adding option to run scan
    parse.add_option('--scan', '-s', default=False, help="This option will run vulnerability scan against the given IP")

    #Adding option to run attack against .....
    parse.add_option('--attack', '-a', default=False, help="This option will run attack against the given IP")

    options, args = parse.parse_args()

    # Run scan script
    if options.scan != False:
        print("Scanning" + options.scan + ":")
        subprocess.call(["prepareClientScan.sh"])
    # Run attack script
    elif options.attack != False:
        print("Performing key reinstallation attack against " + options.attack)
        

if __name__ == '__main__':
    main()


