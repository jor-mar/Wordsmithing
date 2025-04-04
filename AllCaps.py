def main():
    # msg = input(input_message)
    # msg_upper = msg.upper()
    msg_upper = input(input_message).upper()

    if not msg_upper:
        return
    elif msg_upper == printing_statement:
        print('\n'.join(all_inputs), '\n')
    else:
        all_inputs.append(msg_upper)
        print(msg_upper, '\n')
    main()

if __name__ == '__main__':
    input_message = 'Enter a word or phrase you would like to be capitalized: '
    printing_statement = 'print all'.upper()
    all_inputs = []
    main()