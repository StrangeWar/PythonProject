import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pandas
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
               'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    generated_password_list = [choice(letters) for _ in range(randint(4, 6))]
    generated_password_list += [choice(symbols) for _ in range(randint(3, 4))]
    generated_password_list += [choice(numbers) for _ in range(randint(3, 5))]

    shuffle(generated_password_list)
    final_password = "".join(generated_password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, f"{final_password}")
    pyperclip.copy(final_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
website_list = []
email_list = []
password_list = []


def save():
    # getting values from entries
    website = (website_entry.get()).capitalize()
    password = password_entry.get()
    email = email_entry.get()

    password_dict = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # creating a validation dialog box for empty entry.

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="opps", message="Don't leave the entries empty.")

    else:
        # creating a confirmation dialog box.
        is_ok = messagebox.askokcancel(title=f"{website}",
                                       message=f"These are the details  entered:\nemail: {email}\npassword: {password}")

        if is_ok:

            # adding website, email and password in the lists.
            website_list.append(website)
            email_list.append(email)
            password_list.append(password)

            # writing data in a csv file.
            data_dict = {"Website": website_list, "Email/Username": email_list, "Password": password_list}
            data = pandas.DataFrame(data_dict)
            data.to_csv("data.csv", mode="a", index=False, header=False)

            # writing to a text file.
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password}\n")

            # writing to a Json file.
            try:
                with open("data.json", mode="r") as data_file:
                    # reading old data form json file.
                    data = json.load(data_file)

            except JSONDecodeError:
                with open("data.json", mode="w") as data_file:
                    json.dump(password_dict, data_file, indent=4)

            except FileNotFoundError:
                with open("data.json", mode="w") as data_file:
                    json.dump(password_dict, data_file, indent=4)

            else:
                # updating old data with new data
                data.update(password_dict)
                with open("data.json", mode="w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                # clearing entry fields after pressing add button
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- Search ------------------------------- #
def find_password():
    website = (website_entry.get()).capitalize()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No file found.")

    else:
        if website in data:
            searched_email = data[website]["email"]
            searched_password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {searched_email} \nPassword: {searched_password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1,)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.insert(0, "vivekrockss111@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", command=password_generator, borderwidth=1)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, borderwidth=1, width=15)
search_button.grid(column=2, row=1)

window.mainloop()
