from strings import main as tool_strings
from function import tool_cmd

cmd_list = {
        "exit" : tool_cmd.__exit,
        }

def chomp(command): 
    ''' split command and return function and arguments '''
    command = command.strip().split(' ')
    return (command[0], command[1:])

def main():
    print(tool_strings.welcome_banner)
    while True:
        inp = input (">>> ")
        command, args = chomp(inp)
        if command in cmd_list:
            cmd_list[command](args)
        else:
            print(tool_strings.command_not_found)
            #TODO find_next_close_word()


if __name__ == "__main__":
    main()

