def reset():
    cmnd = str(input('\nDo you want to start again? y/n\n'))
    if cmnd == 'y':
        print('Restarting...')
        main()
    if cmnd == 'n':
        print()

def main():
    ins = str(input('Welcome to Lettercase! To start type your sentence below!\n'))
    case = str(input('Now type case to change sentence to: "upper" or "lower"\n'))
    if case == 'lower':
        low = ins.lower()
        print('Your sentence in upper case:', low)
        reset()
    if case == 'upper':
        up = ins.upper()
        print('Your sentence in lower case:', up)
        reset()
main()