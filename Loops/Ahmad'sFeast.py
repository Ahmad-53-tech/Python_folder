name = input("Enter your name: ")
print(f"Hello {name}!")

address = input("Enter your Home Address: ")

phone = input("Enter your phone number: ")

while True:
    print("""
                1. BREAKFAST
                2. LUNCH
                3. DINNER""")

    question = input("What do you care for: ")
    if question == "1":
        print("""
                1. Pancake with Tea- N5,000
                2. Pancake with Coffee- N5,500
                3. Sandwich with Tea - N8,000
                4. Sandwich with Coffee - N8,000
                5. Omelette with Bread - N7,200
                6. Noodles and Egg - N10,000
                7. Waffle with Coffee - N8,000
                8. Waffle with Tea - N8,000
                9. Pap and Fried Plantain - N5,000
                10. Pap and Boiled Plantain - N5,000
                11. Plantain fritata and Zobo - N5,000
                12. Bean Cake with Pap - N5,000
                13. Moi moi with Custard - N7,000
                14. Moi moi with Pap - N10,700
                15. Fried Yam and Egg sauce - N10,000
                16. Boiled Yam and Egg sauce - N10,000
        """)

        meal = input("Enter your preferred meal: ")
        if meal == "1":
            print("You Ordered for Pancake With Tea")

        elif meal == "2":
            print("You Ordered for Pancake with Coffee")

        elif meal == "3":
            print("You Ordered for Sandwich with Tea")

        elif meal == "4":
            print("You Ordered for Sandwich with Coffee")

        elif meal == "5":
            print("You Ordered for Omelette with Bread")

        elif meal == "6":
            print("You Ordered for Noodles and Egg")

        elif meal == "7":
            print("You Ordered for Waffle with Coffee")

        elif meal == "8":
            print("You Ordered for Waffle with Tea")

        elif meal == "9":
            print("You Ordered for Pap and Fried Plantain")

        elif meal == "10":
            print("You Ordered for Pap and Boiled Plantain")

        elif meal == "11":
            print("You Ordered for Plantain Fritata and Zobo")

        elif meal == "12":
            print("You Ordered for Bean cake with Pap")

        elif meal == "13":
            print("You Ordered for Moi moi with Custard")

        elif meal == "14":
            print("You Ordered for Moi moi with Pap")

        elif meal == "15":
            print("You Ordered for Fried yam and Egg sauce")

        elif meal == "16":
            print("You Ordered for Boiled yam and Egg sauce")

        else:
            continue

        print(f"""
                    1. Pay on Delivery
                    2. Transfer""")

        mode_of_payment = input("Mode of payment: ")
        if mode_of_payment == "1":
            print(f"Your meal will be delivered to No.{address} in 10 minutes")

            print("""
            Mr Obi: 09027372436 (Delivery Agent)
            Call this number in case of changed Address""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                continue

            elif message == "n":
                print("THANKS FOR YOUR PATRONAGE")

                print("""How was our service?

                                                1. Not Satisfactory
                                                2. Satisfactory
                                                3. Very Satisfactory
                                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")

                    print("""
                                                    1. Slow Delivery
                                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                    Thank you so much for your kind words!
                    We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                    AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                    Wow! Thank you for your amazing review! 
                    We're thrilled you had such a great experience and can't wait to serve you again!" 
                    AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
            break



        elif mode_of_payment == "2":
            print("""Pay to this account"

                  4206041380
                  AHMAD'S FEAST
                  PYTHON BANK""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                print("PAYMENT SUCCESSFUL!")
                continue

            elif message == "n":
                print(f"""
                PAYMENT SUCCESSFUL!
                Your meal will be delivered to No.{address} in 10 minutes""")

                print("""
                            Mr Obi: 09027372436 (Delivery Agent)
                            Call this number in case of changed Address""")
                print("THANKS FOR YOUR PATRONAGE")
                print("""How was our service?

                                1. Not Satisfactory
                                2. Satisfactory
                                3. Very Satisfactory
                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")
                    print("""
                                    1. Slow Delivery
                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                        Thank you so much for your kind words!
                        We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                        AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                        Wow! Thank you for your amazing review! 
                        We're thrilled you had such a great experience and can't wait to serve you again!" 
                        AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
            break

    if question == "2":
        print("""
                        1. Fried Rice and Chicken - N15,000
                        2. Champagne Rice with Turkey - N14,000
                        3. Jollof Rice with Beef - N11,000
                        4. Porridge Yam with Fried Fish - N11,000
                        5. Native Rice with Goat Meat - N15,000
                        6. White Rice with Ofada Sauce - N12,000
                        7. Egusi Soup with Semo - N14,000
                        8. Okra Soup with Eba - N13,000
                        9. Nsala Soup with Pounded Yam - N15,000
                        10.Bitter leaf soup with Pounded Yam - N16,000
                        11.Pounded Yam with Pepper soup - N23,000
                        12.Chinese Rice with Peppered Chicken - N25,000
                """)

        meal = input("Enter your preferred meal: ")
        if meal == "1":
            print("You Ordered for Fried Rice and Chicken")

        elif meal == "2":
            print("You Ordered for Champagne Rice with Turkey")

        elif meal == "3":
            print("You Ordered for Jollof Rice with Beef")

        elif meal == "4":
            print("You Ordered for Porridge Yam with Fried Fish")

        elif meal == "5":
            print("You Ordered for Native Rice with Goat Meat")

        elif meal == "6":
            print("You Ordered for White Rice with Ofada Sauce")

        elif meal == "7":
            print("You Ordered for Egusi Soup with Semo")

        elif meal == "8":
            print("You Ordered for Okra Soup with Eba")

        elif meal == "9":
            print("You Ordered for Nsala Soup with Pounded Yam")

        elif meal == "10":
            print("You Ordered for Bitter leaf soup with Pounded Yam")

        elif meal == "11":
            print("You Ordered for Pounded Yam with Pepper soup")

        elif meal == "12":
            print("You Ordered for Chinese Rice with Peppered Chicken")

        else:
            continue

        print(f"""
                            1. Pay on Delivery
                            2. Transfer""")

        mode_of_payment = input("Mode of payment: ")
        if mode_of_payment == "1":
            print(f"Your meal will be delivered to No.{address} in 10 minutes")
            print("""
            Mr Alexis: 08113432436 (Delivery Agent)
            Call this number in case of changed Address""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                continue

            elif message == "n":
                print("THANKS FOR YOUR PATRONAGE")
                print("""How was our service?

                                                1. Not Satisfactory
                                                2. Satisfactory
                                                3. Very Satisfactory
                                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")
                    print("""
                                                    1. Slow Delivery
                                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                         Thank you so much for your kind words!
                         We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                         AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                          Wow! Thank you for your amazing review! 
                          We're thrilled you had such a great experience and can't wait to serve you again!" 
                          AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
            break


        elif mode_of_payment == "2":
            print("""Pay to this account"
                    4206041380
                    AHMAD'S FEAST
                    PYTHON BANK""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                print("PAYMENT SUCCESSFUL!")
                continue

            elif message == "n":
                print(f"""
                PAYMENT SUCCESSFUL!
                Your meal will be delivered to No.{address} in 10 minutes""")
                print("""
                            Mr Alexis: 08113432436 (Delivery Agent)
                            Call this number in case of changed Address""")
                print("THANKS FOR YOUR PATRONAGE")
                print("""How was our service?

                                                1. Not Satisfactory
                                                2. Satisfactory
                                                3. Very Satisfactory
                                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")
                    print("""
                                                    1. Slow Delivery
                                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                    Thank you so much for your kind words!
                    We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                    AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                    Wow! Thank you for your amazing review! 
                    We're thrilled you had such a great experience and can't wait to serve you again!" 
                    AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
            break

    if question == "3":
        print("""
                             1. Noodles with Egg - N5,000
                             2. Fruit Salad - N7,000
                             3. Beans and Plantain - N8,500
                             4. Meat Pie and Ice Cream - N8,000
                             5. Meat Pie and Fruit Juice - N10,000
                             6. Smoothie - N10,000
                             7. Chicken Pie and Ice Cream - N8,000
                             8. Plantain Chips with Juice - N10,000
                             9. Sausage with Ice Cream - N7,000
                             10.Porridge Plantain with Dry Fish - N10,000                             
                     """)

        meal = input("Enter your preferred meal: ")
        if meal == "1":
            print("You Ordered for Noodles with Egg")

        elif meal == "2":
            print("You Ordered for Fruit Salad")

        elif meal == "3":
            print("You Ordered for Beans and Plantain")

        elif meal == "4":
            print("You Ordered for Meat Pie and Ice Cream")

        elif meal == "5":
            print("You Ordered for Meat Pie and Fruit Juice")

        elif meal == "6":
            print("You Ordered for Smoothie")

        elif meal == "7":
            print("You Ordered for Chicken Pie and Ice Cream")

        elif meal == "8":
            print("You Ordered for Plantain Chips with Juice")

        elif meal == "9":
            print("You Ordered for Sausage with Ice Cream")

        elif meal == "10":
            print("You Ordered for Porridge Plantain with Dry Fish")

        else:
            continue

        print(f"""
                                 1. Pay on Delivery
                                 2. Transfer""")

        mode_of_payment = input("What is your mode of payment: ")
        if mode_of_payment == "1":
            print(f"Your meal will be delivered to No.{address} in 10 minutes")
            print("""
            Mr Habeeb: 08112302436 (Delivery Agent)
            Call this number in case of changed Address""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                continue

            elif message == "n":
                print("THANKS FOR YOUR PATRONAGE")
                print("""How was our service?

                                                1. Not Satisfactory
                                                2. Satisfactory
                                                3. Very Satisfactory
                                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")
                    print("""
                                                    1. Slow Delivery
                                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                    Thank you so much for your kind words!
                    We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                    AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                    Wow! Thank you for your amazing review! 
                    We're thrilled you had such a great experience and can't wait to serve you again!" 
                    AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
            break


        elif mode_of_payment == "2":
            print("""Pay to this account"
                               4206041380
                               AHMAD'S FEAST
                               PYTHON BANK""")

            message = input("Will you like to order more(y - yes / n - no): ").lower()
            if message == "y":
                print("PAYMENT SUCCESSFUL!")
                continue

            elif message == "n":
                print(f"""
                PAYMENT SUCCESSFUL!
                Your meal will be delivered to {address} in 10 minutes""")
                print("""
                    Mr Habeeb: 08112302436 (Delivery Agent)
                    Call this number in case of changed Address""")
                print("THANKS FOR YOUR PATRONAGE")
                print("""How was our service?

                                                1. Not Satisfactory
                                                2. Satisfactory
                                                3. Very Satisfactory
                                                """)

                satisfactory = input("Satisfactory level: ")
                if satisfactory == "1":
                    print("😥")
                    print("""
                                                    1. Slow Delivery
                                                    2. Bad Meal""")

                    bad = input("Reason: ")
                    if bad == "1":
                        print(f"""
                        ☹️We sincerely apologize for the slow delivery. 
                        We’re working on improving our service to get your food to you faster. Thank you for your patience and support!""")

                    elif bad == "2":
                        print(f"""
                        ☹️We’re really sorry you didn’t enjoy your meal.
                        We appreciate your feedback and would love the chance to make it right. Please contact us on this email (ahmadfeast@gmail.com)
                        to let us know how we can improve!""")

                    else:
                        print("Contact us on this email (ahmadfeast@gmail.com) to let us know how we can improve")


                elif satisfactory == "2":
                    print(f"""
                    Thank you so much for your kind words!
                    We're glad you enjoyed your meal and appreciate your support. Hope to serve you again soon!
                    AHMAD'S FEAST *Feast with us🍽️😋🤗""")

                elif satisfactory == "3":
                    print(f"""
                    Wow! Thank you for your amazing review! 
                    We're thrilled you had such a great experience and can't wait to serve you again!" 
                    AHMAD'S FEAST *Feast with us🍽️😋🤗*""")
                break