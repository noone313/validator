class Validator:


    def Email(email):

        not_valid_chars = []

        valid_status = False

        at = email.count('@')
        
        if at != 1 :
            not_valid_chars.append(at)
            return valid_status , not_valid_chars
        
        else:
            email_name, domain = email.split('@')

        email_name_valid_chars = []

        domain_valid_chars = []

        
        
        for i in range(len(email_name)):

            if email_name[i] in [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]:
                email_name_valid_chars.append(email_name[i])
                # print(f'email char {email_name_valid_chars[i]} is valid')

            else:
                not_valid_chars.append(email_name[i])

        for i in range(len(domain)):

            if domain[i] in [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)]+ ['.']:
                domain_valid_chars.append(domain[i])
                # print(f'domain char {domain_valid_chars[i]} is valid')

            else:
                not_valid_chars.append(domain[i])

        dot_count = domain.count('.')
        
        if dot_count != 1:
            not_valid_chars.append(dot_count)

        if len(not_valid_chars) > 0:
            valid_status = False

        else:
            valid_status = True
        
        if len(not_valid_chars) > 0 :
            return valid_status , not_valid_chars
        else:
            return valid_status
        



    def Password(password):
        
        str_password = str(password)

        password_numbers = list(str_password)

        if len(password_numbers) < 8 :
            return False, 'length of password is short'

        if not password_numbers[0].isupper():
            return False, 'first char should be capital'
        
        has_digit = False

        for char in password_numbers:
            
            if char.isdigit():
                has_digit = True
                
        
        if not has_digit:
            return False, 'number requaired'
        

        
        return True
        

validator = Validator



