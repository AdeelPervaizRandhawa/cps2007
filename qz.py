import tkinter as tk
from tkinter import ttk, messagebox
import uuid
import json
from datetime import datetime, timedelta

class GymManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("St. Mary's Fitness Management System")
        self.root.geometry("1000x700")

        # Data storage
        self.data_file = "gym_data.json"
        self.load_data()

        # Main menu
        self.main_menu()

    def load_data(self):
        try:
            with open(self.data_file, "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {"locations": [], "members": [], "workout_zones": [], "appointments": [], "payments": []}

    def save_data(self):
        with open(self.data_file, "w") as file:
            json.dump(self.data, file, indent=4)

    def main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="St. Mary's Fitness Management System", font=("Helvetica", 18, "bold")).pack(pady=20)

        tk.Button(self.root, text="1. Add Gym Location", command=self.add_gym_location, width=40).pack(pady=5)
        tk.Button(self.root, text="2. Add Member", command=self.add_member, width=40).pack(pady=5)
        tk.Button(self.root, text="3. Add Workout Zone", command=self.add_workout_zone, width=40).pack(pady=5)
        tk.Button(self.root, text="4. Manage Appointments", command=self.manage_appointments, width=40).pack(pady=5)
        tk.Button(self.root, text="5. Record Payments", command=self.record_payments, width=40).pack(pady=5)
        tk.Button(self.root, text="6. Track Attendance", command=self.track_attendance, width=40).pack(pady=5)
        tk.Button(self.root, text="7. View Reports", command=self.view_reports, width=40).pack(pady=5)
        tk.Button(self.root, text="8. Exit", command=self.save_and_exit, width=40).pack(pady=5)

    def add_gym_location(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Gym Location", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Location Name:").pack()
        location_name_entry = tk.Entry(self.root)
        location_name_entry.pack()

        tk.Label(self.root, text="City:").pack()
        city_entry = tk.Entry(self.root)
        city_entry.pack()

        def save_location():
            name = location_name_entry.get()
            city = city_entry.get()

            if name and city:
                location = {
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "city": city,
                    "members": [],
                    "zones": []
                }
                self.data["locations"].append(location)
                self.save_data()
                messagebox.showinfo("Success", "Gym location added successfully!")
                self.main_menu()
            else:
                messagebox.showwarning("Input Error", "Please fill all fields.")

        tk.Button(self.root, text="Save", command=save_location).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def add_member(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Member", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Member Name:").pack()
        member_name_entry = tk.Entry(self.root)
        member_name_entry.pack()

        tk.Label(self.root, text="Age:").pack()
        age_entry = tk.Entry(self.root)
        age_entry.pack()

        tk.Label(self.root, text="Membership Type (Regular/Premium/Trial):").pack()
        membership_type_entry = tk.Entry(self.root)
        membership_type_entry.pack()

        tk.Label(self.root, text="Gym Location:").pack()
        gym_location_combobox = ttk.Combobox(self.root, values=[loc["name"] for loc in self.data["locations"]])
        gym_location_combobox.pack()

        def save_member():
            name = member_name_entry.get()
            age = age_entry.get()
            membership_type = membership_type_entry.get()
            gym_location_name = gym_location_combobox.get()

            if name and age.isdigit() and membership_type and gym_location_name:
                member = {
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "age": int(age),
                    "type": membership_type,
                    "attendance": [],
                    "subscriptions": []
                }
                for location in self.data["locations"]:
                    if location["name"] == gym_location_name:
                        location["members"].append(member)
                        break
                self.data["members"].append(member)
                self.save_data()
                messagebox.showinfo("Success", "Member added successfully!")
                self.main_menu()
            else:
                messagebox.showwarning("Input Error", "Please fill all fields correctly.")

        tk.Button(self.root, text="Save", command=save_member).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def add_workout_zone(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Add Workout Zone", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Zone Name:").pack()
        zone_name_entry = tk.Entry(self.root)
        zone_name_entry.pack()

        tk.Label(self.root, text="Zone Type:").pack()
        zone_type_entry = tk.Entry(self.root)
        zone_type_entry.pack()

        tk.Label(self.root, text="Gym Location:").pack()
        gym_location_combobox = ttk.Combobox(self.root, values=[loc["name"] for loc in self.data["locations"]])
        gym_location_combobox.pack()

        def save_zone():
            name = zone_name_entry.get()
            zone_type = zone_type_entry.get()
            gym_location_name = gym_location_combobox.get()

            if name and zone_type and gym_location_name:
                zone = {
                    "id": str(uuid.uuid4()),
                    "name": name,
                    "type": zone_type
                }
                for location in self.data["locations"]:
                    if location["name"] == gym_location_name:
                        location["zones"].append(zone)
                        break
                self.data["workout_zones"].append(zone)
                self.save_data()
                messagebox.showinfo("Success", "Workout zone added successfully!")
                self.main_menu()
            else:
                messagebox.showwarning("Input Error", "Please fill all fields.")

        tk.Button(self.root, text="Save", command=save_zone).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def manage_appointments(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Manage Appointments", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Member:").pack()
        member_combobox = ttk.Combobox(self.root, values=[member["name"] for member in self.data["members"]])
        member_combobox.pack()

        tk.Label(self.root, text="Appointment Type:").pack()
        appointment_type_entry = tk.Entry(self.root)
        appointment_type_entry.pack()

        tk.Label(self.root, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(self.root)
        date_entry.pack()

        def save_appointment():
            member_name = member_combobox.get()
            appointment_type = appointment_type_entry.get()
            date = date_entry.get()

            if member_name and appointment_type and date:
                for member in self.data["members"]:
                    if member["name"] == member_name:
                        appointment = {
                            "id": str(uuid.uuid4()),
                            "member_id": member["id"],
                            "type": appointment_type,
                            "date": date
                        }
                        self.data["appointments"].append(appointment)
                        self.save_data()
                        messagebox.showinfo("Success", "Appointment added successfully!")
                        self.main_menu()
                        return
                messagebox.showwarning("Error", "Member not found.")
            else:
                messagebox.showwarning("Input Error", "Please fill all fields.")

        tk.Button(self.root, text="Save", command=save_appointment).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def record_payments(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Record Payments", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Member:").pack()
        member_combobox = ttk.Combobox(self.root, values=[member["name"] for member in self.data["members"]])
        member_combobox.pack()

        tk.Label(self.root, text="Amount:").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        tk.Label(self.root, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(self.root)
        date_entry.pack()

        def save_payment():
            member_name = member_combobox.get()
            amount = amount_entry.get()
            date = date_entry.get()

            if member_name and amount.isdigit() and date:
                for member in self.data["members"]:
                    if member["name"] == member_name:
                        payment = {
                            "id": str(uuid.uuid4()),
                            "member_id": member["id"],
                            "amount": float(amount),
                            "date": date
                        }
                        self.data["payments"].append(payment)
                        self.save_data()
                        messagebox.showinfo("Success", "Payment recorded successfully!")
                        self.main_menu()
                        return
                messagebox.showwarning("Error", "Member not found.")
            else:
                messagebox.showwarning("Input Error", "Please fill all fields correctly.")

        tk.Button(self.root, text="Save", command=save_payment).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def track_attendance(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Track Attendance", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text="Member:").pack()
        member_combobox = ttk.Combobox(self.root, values=[member["name"] for member in self.data["members"]])
        member_combobox.pack()

        tk.Label(self.root, text="Workout Zone:").pack()
        zone_combobox = ttk.Combobox(self.root, values=[zone["name"] for zone in self.data["workout_zones"]])
        zone_combobox.pack()

        tk.Label(self.root, text="Date (YYYY-MM-DD):").pack()
        date_entry = tk.Entry(self.root)
        date_entry.pack()

        def save_attendance():
            member_name = member_combobox.get()
            zone_name = zone_combobox.get()
            date = date_entry.get()

            if member_name and zone_name and date:
                for member in self.data["members"]:
                    if member["name"] == member_name:
                        attendance = {
                            "id": str(uuid.uuid4()),
                            "member_id": member["id"],
                            "zone": zone_name,
                            "date": date
                        }
                        member["attendance"].append(attendance)
                        self.save_data()
                        messagebox.showinfo("Success", "Attendance tracked successfully!")
                        self.main_menu()
                        return
                messagebox.showwarning("Error", "Member not found.")
            else:
                messagebox.showwarning("Input Error", "Please fill all fields.")

        tk.Button(self.root, text="Save", command=save_attendance).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def view_reports(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="View Reports", font=("Helvetica", 16)).pack(pady=20)

        tk.Label(self.root, text=f"Total Members: {len(self.data['members'])}").pack()
        tk.Label(self.root, text=f"Total Gym Locations: {len(self.data['locations'])}").pack()
        tk.Label(self.root, text=f"Total Appointments: {len(self.data['appointments'])}").pack()
        tk.Label(self.root, text=f"Total Payments Recorded: {len(self.data['payments'])}").pack()

        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=10)

    def save_and_exit(self):
        self.save_data()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = GymManagementSystem(root)
    root.mainloop()
