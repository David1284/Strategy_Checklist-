import sys
import urllib.request
from PIL import ImageTk, Image
import tkinter as tk
from io import BytesIO


def mystrategy():
    global break_structure, valid_ob, divergence

    print("My Strategies:")
    print("\n\n1. Supply and demand (S.B.V)")
    print("2. Supply and demand (O.B.V)")
    print("3. Supply and demand (R.B.R)")
    print("4. ATM Strategy (london open )")
    print("5. Fibonacci strategy")
    print("\nUse wyckoff, Market maker models and trends to validate your setup. ")

    selected_strategy = None
    while selected_strategy not in ["1", "2", "3", "4", "5"]:
        # Prompt the user for their selection
        selected_strategy = input("\n\nSelect the strategy currently playing out in the market (enter the number): ")

    "-----------------------------------------------------------------------------------------------------------------"
    # Validate the user input and print the selected strategy
    if selected_strategy == "1":
        print("\nS.B.V - Strategy")

        while True:
            sweep_high = input("\nIs there a sweep of the previous high/low ? (yes/no): ")
            if sweep_high.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            break_structure = input("Did the price break structure? (yes/no): ")
            if break_structure.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            valid_ob = input("Is there a valid order block or consolidation area? (yes/no): ")
            if valid_ob.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            break


        if sweep_high.lower() == "yes" and break_structure.lower() == "yes" and valid_ob.lower() == "yes":
            print("\n\nchecking for red flags and Blockers......")
            red_flag1 = input("\n\nIs the retracement caused by an area of major support or resistance ? (yes/no): ")
            if red_flag1.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            red_flag2 = input("Is the price Retracing from a pyscological level? (yes/no): ")
            if red_flag2.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            red_flag3 = input("Is the price coming from a second OB in an opposing order flow ? (yes/no): ")
            if red_flag3.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            else:
                print("\n\nTAKE THE TRADE !!!!!")
                print("\nStats:")
                print("This is a Grade A setup")
                print("Probability of success is 4/5")
                print("Risk 1%")
                print("Risk:Reward ratio = 1:3")
        else:
            print("\n\nDO NOT TAKE THE TRADE NO MATTER WHAT")
            sys.exit()

    # "O.B.V Strategy"
    elif selected_strategy == "2":
        print("\nO.B.V - Strategy")
        while True:
            break_structure = input("\nDid the price break the structure? (yes/no): ")
            if break_structure.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            valid_ob = input("Is there a valid order block or consolidation area? (yes/no): ")
            if valid_ob.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            divergence = input("Is there a valid divergence? (yes/no): ")
            if divergence.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            break


        if divergence.lower() == "yes" and break_structure.lower() == "yes" and valid_ob.lower() == "yes":
            print("\n\nchecking for red flags and Blockers......")
            ob_red_flag1 = input("\n\nIs the retracement caused by an area of major support or resistance ? (yes/no): ")
            if ob_red_flag1.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            ob_red_flag2 = input("Is the retracement caused by a psycological level ?(yes/no): ")
            if ob_red_flag2.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            ob_red_flag3 = input("Is the price coming from a second OB in a an opposing order flow ? (yes/no): ")
            if ob_red_flag3.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()
            else:
                print("\n\nTAKE THE TRADE !!!!!")
                print("\nStats:")
                print("This is a Grade A setup")
                print("Probability of success is 4/5")
                print("Risk 1%")
                print("Risk:Reward ratio = 1:3")
        else:
            print("\n\nDO NOT TAKE THE TRADE NO MATTER WHAT")
            sys.exit()


    #R.B.R and supply to demand Transfer
    elif selected_strategy == "3":
        while True:
            SnD_transfer = input("\nis there a previous supply or demand that is in line with the current S/D ? (yes/no): ")
            if SnD_transfer.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue

            break_structure = input("Is there a break of structure ? (yes/no): ")
            if break_structure.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            break
        success_probability = ""
        if SnD_transfer.lower() == "yes":
            if break_structure.lower() == "yes":
                success_probability = "higher"
            else:
                success_probability = "high"
            print("\n\nchecking for red flags....")
            Optimal_snd = input("Is there a better discounted level of supply or demand? (yes/no): ")
            if Optimal_snd.lower() == "yes":
                print("Don't take the trade, Wait for price to get to the more discounted SnD level ")
                sys.exit()

            rbr_red_flag2 = input("Is the retracement caused by an area of major support or resistance ? (yes/no): ")
            if rbr_red_flag2.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            rbr_red_flag3 = input("Is the retracement caused by a psycological level ?(yes/no): ")
            if rbr_red_flag3.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            rbr_red_flag4 = input("Is the retracement coming from a 15 mins RBR or OB? (yes/no): ")
            if rbr_red_flag4.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()

            rbr_red_flag5 = input("Is the retracement caused by an SM ? (yes/no): ")
            if rbr_red_flag5.lower() == "yes":
                print("DO NOT TAKE THE TRADE NO MATTER WHAT")
                sys.exit()
            elif success_probability == "higher":
                print("\n\nTAKE THE TRADE !!!!!")
                print("\nStats:")
                print("This is a Grade A setup")
                print("Probability of success is 5/5")
                print("Risk 1%")
                print("Risk:Reward ratio = 1:3")
            else:
                print("\n\nTAKE THE TRADE   !!!!!")
                print("\nStats:")
                print("This is a Grade A setup")
                print("Probability of success is 4/5")
                print("Risk 0.5%")
                print("Risk:Reward ratio = 1:3")
        else:
            print("\n\nDO NOT TAKE THE TRADE NO MATTER WHAT")
            sys.exit()
        print("Still in progress... All you need is a supply to demand transfer")

    #Fibbonacci Strategy
    elif selected_strategy == "4":
        while True:
            Impulse = input("\nIs there a good impulse in the market ? (yes/no): ")
            if Impulse.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue

            Retracement = input("Is there a break of structure ? (yes/no): ")
            if Retracement.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue

            trend = input("Is the market in the direction of the 15 minutes and 30 mins trend ? (yes/no): ")
            if trend.lower() not in ["yes", "no"]:
                print("Invalid entry. Please try again.")
                continue
            break



# ---------------------------------------------------------------------------------------------------------------------------
#         if Impulse.lower() == "yes" and Retracement.lower() == "yes" and trend.lower() == "yes":
#             print("\n\nchecking for red flags and Blockers......")
#             ob_red_flag1 = input("\n\nIs the retracement caused by an area of major support or resistance ? (yes/no): ")
#             if ob_red_flag1.lower() == "yes":
#                 print("DO NOT TAKE THE TRADE NO MATTER WHAT")
#                 sys.exit()
#
#             ob_red_flag2 = input("Is the retracement caused by a psycological level ?(yes/no): ")
#             if ob_red_flag2.lower() == "yes":
#                 print("DO NOT TAKE THE TRADE NO MATTER WHAT")
#                 sys.exit()
#
#             ob_red_flag3 = input("Is the price coming from a second OB in a an opposing order flow ? (yes/no): ")
#             if ob_red_flag3.lower() == "yes":
#                 print("DO NOT TAKE THE TRADE NO MATTER WHAT")
#                 sys.exit()
#             else:
#                 print("\n\nTAKE THE TRADE !!!!!")
#                 print("\nStats:")
#                 print("This is a Grade A setup")
#                 print("Probability of success is 4/5")
#                 print("Risk 1%")
#                 print("Risk:Reward ratio = 1:3")
#         else:
#             print("\n\nDO NOT TAKE THE TRADE NO MATTER WHAT")
#             sys.exit()
# ----------------------------------------------------------------------------------------------------------------------

def show_image_from_url(url):
    # Retrieve the image from the URL
    image_data = urllib.request.urlopen(url).read()
    # Create a Tkinter window
    window = tk.Tk()
    # Create an Image object from the retrieved data
    image = Image.open(BytesIO(image_data))
    # Create a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)
    # Create a label to display the image
    label = tk.Label(window, image=photo)
    label.pack()
    # Run the Tkinter event loop
    window.mainloop()

def confluences():
    print("Confluences for supply and dmenad")
    print("\n\nConfluences for Fibbonaci")

def red_flags():
    print("Supply and demand Red Flags")
    print("1.) Retracement caused By support or resistance")
    print("2.) Retracement caused by Pscycological level")
    print("3.) Supply to demand Transfer within a HTF breaker Block")

    print("\n\nFibbonaci Red flag")


def Trading_information():
    print("Highest Probabilistic setup ")
    print("1. 15 Mins Supply to demand transfer after a break of structure")
    print("2. Higher high then lower lower and Orderblock at OTE")
    print("3. 1/2 minutes S.B.V within a 15 mins SnD Transfer")

    print("ULTIMATE: 15 mins supply to demand transger after a BOS "
          "+ Higher high then lower lower and Orderblock at OTE")

def Morning_Trading_routine():
    print("Draw supplly and demand levels from the 15 minutes Timeframe")
    print("Mark out Dsicounted and premium levels Using the Gatt pattern")
    print("Identify the current wyckooff schematic or Phase the pair is in")

def Night_Trading_routine():
    print("Draw supplly and demand levels from the 15 minutes Timeframe")
    print("Mark out Dsicounted and premium levels Using the Gatt pattern")
    print("Identify the current wyckooff schematic or Phase the pair is in")


lambo = "https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini" \
      "/facelift_2019/models_gw/2023/03_29_revuelto/gate_models_s_02_m.jpg"
sbv_url = "https://drive.google.com/file/d/1obTjne8UR6CkkUZnUEOErqsHMuhNK2Ta/view?usp=sharing"
OBV_url = ""
RBR_url = ""
#show_image_from_url(sbv_url)


# Call the function
mystrategy()


