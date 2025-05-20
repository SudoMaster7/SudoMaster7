import tkinter as tk
from tkinter import ttk

# Main application file
# if __name__ == "__main__": # Commented out for testability, GUI launched by main_gui_app
    # Create the main window
    # root = tk.Tk() # Moved to main_gui_app
    # root.title("Patient Management and Scheduling System")

    # Create a Notebook widget
    # notebook = ttk.Notebook(root) # Moved to main_gui_app

    # Create frames for each tab
    # patient_management_frame = ttk.Frame(notebook) # Moved to main_gui_app
    # appointment_scheduling_frame = ttk.Frame(notebook) # Moved to main_gui_app

import csv
import os
from tkinter import messagebox # Using messagebox for simple dialogs

# --- Global Variables ---
PATIENTS_FILE = "data/patients.csv"
PATIENTS_HEADER = ["PatientID", "Name", "Contact", "Address"]
APPOINTMENTS_FILE = "data/appointments.csv"
APPOINTMENTS_HEADER = ["AppointmentID", "PatientID", "Date", "Time", "Reason"]

# --- Helper Functions ---
def initialize_patients_file():
    """Creates patients.csv with a header if it doesn't exist or is empty."""
    if not os.path.exists(PATIENTS_FILE) or os.path.getsize(PATIENTS_FILE) == 0:
        with open(PATIENTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(PATIENTS_HEADER)

def get_next_patient_id():
    """Generates the next sequential PatientID."""
    initialize_patients_file() # Ensure file and header exist
    try:
        with open(PATIENTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            last_id = 0
            for row in reader:
                if row and row[0].isdigit(): # Check if row is not empty and ID is a digit
                    last_id = int(row[0])
            return last_id + 1
    except FileNotFoundError:
        return 1
    except StopIteration: # File exists but is empty (no header, no data)
        return 1
    except csv.Error as e:
        print(f"CSV Error reading patient ID from {PATIENTS_FILE}: {e}")
        raise
    except Exception as e:
        print(f"Error reading patient ID from {PATIENTS_FILE}: {e}") 
        return 1 

def initialize_appointments_file():
    """Creates appointments.csv with a header if it doesn't exist or is empty."""
    if not os.path.exists(APPOINTMENTS_FILE) or os.path.getsize(APPOINTMENTS_FILE) == 0:
        with open(APPOINTMENTS_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(APPOINTMENTS_HEADER)

def get_next_appointment_id():
    """Generates the next sequential AppointmentID."""
    initialize_appointments_file()
    try:
        with open(APPOINTMENTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            last_id = 0
            for row in reader:
                if row and row[0].isdigit():
                    last_id = int(row[0])
            return last_id + 1
    except FileNotFoundError:
        return 1
    except StopIteration: # File exists but is empty
        return 1
    except csv.Error as e:
        print(f"CSV Error reading appointment ID from {APPOINTMENTS_FILE}: {e}")
        raise
    except Exception: 
        return 1 

# --- Patient Data Cache ---
patient_name_cache = {} 

def load_patient_name_cache():
    """Loads patient IDs and names into a cache for quick lookup."""
    patient_name_cache.clear()
    try:
        initialize_patients_file()
        if not os.path.exists(PATIENTS_FILE) or os.path.getsize(PATIENTS_FILE) == 0:
            return 
        
        with open(PATIENTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            try:
                header = next(reader) 
                if list(header) != PATIENTS_HEADER:
                    print(f"Warning: {PATIENTS_FILE} header mismatch during cache load.")
                    return 
            except StopIteration: 
                return 

            for i, row in enumerate(reader):
                try:
                    if row and len(row) >= 2: 
                        patient_name_cache[row[0]] = row[1]
                except IndexError:
                    print(f"Warning: Row {i+2} in {PATIENTS_FILE} is malformed (not enough columns). Skipping.")
                except csv.Error as e:
                    print(f"CSV parsing error in {PATIENTS_FILE} at row {i+2}: {e}. Skipping row.")
                    continue
    except FileNotFoundError:
        pass
    except csv.Error as e: 
        print(f"CSV Error loading patient name cache from {PATIENTS_FILE}: {e}")
        # In a real GUI, this might set a status bar message
        # if 'pm_message_var' in globals() and pm_message_var: 
        #     pm_message_var.set(f"Error: {PATIENTS_FILE} is corrupted or unreadable.")
    except Exception as e:
        print(f"Error loading patient name cache: {e}")
        # if 'pm_message_var' in globals() and pm_message_var:
        #      pm_message_var.set(f"Unexpected error loading patient data.")

# --- Module-Level Helper Functions (can be used by GUI and tests) ---
def update_patient_appointment_count(patient_id_str, target_tk_stringvar):
    """
    Calculates and updates the appointment count label for a given patient ID.
    Args:
        patient_id_str: The patient ID (string).
        target_tk_stringvar: The Tkinter StringVar to update with the count.
    """
    if not patient_id_str:
        if target_tk_stringvar: target_tk_stringvar.set("Appointments: N/A")
        return
        
    count = 0
    try:
        initialize_appointments_file()
        if not os.path.exists(APPOINTMENTS_FILE) or os.path.getsize(APPOINTMENTS_FILE) == 0:
            if target_tk_stringvar: target_tk_stringvar.set("Appointments: 0")
            return

        with open(APPOINTMENTS_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            try:
                header = next(reader) 
                if list(header) != APPOINTMENTS_HEADER:
                    if target_tk_stringvar: target_tk_stringvar.set("Appointments: File format error")
                    print(f"Error: {APPOINTMENTS_FILE} header incorrect during count.")
                    return
            except StopIteration: 
                if target_tk_stringvar: target_tk_stringvar.set("Appointments: 0")
                return
            except csv.Error as e:
                if target_tk_stringvar: target_tk_stringvar.set("Appointments: File read error")
                print(f"Error reading {APPOINTMENTS_FILE} header during count: {e}")
                return

            for i, row_data in enumerate(reader):
                try:
                    if row_data and len(row_data) > 1 and row_data[1] == patient_id_str: 
                        count += 1
                except IndexError:
                    print(f"Warning: Row {i+2} in {APPOINTMENTS_FILE} is malformed for count. Skipping.")
        if target_tk_stringvar: target_tk_stringvar.set(f"Appointments: {count}")
    except FileNotFoundError:
        if target_tk_stringvar: target_tk_stringvar.set("Appointments: 0")
    except csv.Error as e:
        print(f"CSV Error reading appointments for count: {e}")
        if target_tk_stringvar: target_tk_stringvar.set("Appointments: File error")
    except Exception as e:
        print(f"Error reading appointment count: {e}")
        if target_tk_stringvar: target_tk_stringvar.set("Appointments: Error")

# --- Main Application ---
def main_gui_app(): 
    root = tk.Tk()
    root.title("Patient Management and Scheduling System")

    # --- Variables ---
    name_var = tk.StringVar()
    contact_var = tk.StringVar()
    address_var = tk.StringVar()
    pm_message_var = tk.StringVar() 
    selected_patient_id_for_edit = None 
    patient_appt_count_var = tk.StringVar(value="Appointments: N/A")

    appointment_patient_var = tk.StringVar()
    appointment_date_var = tk.StringVar()
    appointment_time_var = tk.StringVar()
    appointment_reason_var = tk.StringVar()
    as_message_var = tk.StringVar() 
    selected_appt_id_for_edit = None 
    patient_combobox_map = {} 

    # --- Functions for Patient Management ---
    def load_selected_patient_to_form(event=None):
        nonlocal selected_patient_id_for_edit 
        selected_item = patient_tree.focus() 
        if selected_item:
            patient_data = patient_tree.item(selected_item, "values")
            if patient_data and len(patient_data) == len(PATIENTS_HEADER):
                selected_patient_id_for_edit = patient_data[0] 
                name_var.set(patient_data[1])
                contact_var.set(patient_data[2])
                address_var.set(patient_data[3])
                pm_message_var.set(f"Patient ID {selected_patient_id_for_edit} loaded for editing.")
                update_patient_appointment_count(selected_patient_id_for_edit, patient_appt_count_var)
            else:
                pm_message_var.set("Could not load patient data. Selection invalid.")
                selected_patient_id_for_edit = None
                patient_appt_count_var.set("Appointments: N/A") 
        else:
            if not patient_tree.focus(): 
                name_var.set("")
                contact_var.set("")
                address_var.set("")
                pm_message_var.set("No patient selected or selection cleared.")
                selected_patient_id_for_edit = None
                patient_appt_count_var.set("Appointments: N/A")

    def view_patients():
        for item in patient_tree.get_children():
            patient_tree.delete(item)
        initialize_patients_file() 
        try:
            with open(PATIENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                try:
                    header = next(reader) 
                    if list(header) != PATIENTS_HEADER:
                        pm_message_var.set(f"Error: {PATIENTS_FILE} header is incorrect. Please check the file or delete it to reset.")
                        return
                except StopIteration: 
                    pm_message_var.set("No patient data found.") 
                    return 
                except csv.Error as e:
                    pm_message_var.set(f"Error reading {PATIENTS_FILE} header: {e}. File might be corrupted.")
                    return

                for i, row in enumerate(reader):
                    try:
                        if row and len(row) == len(PATIENTS_HEADER): 
                            patient_tree.insert("", tk.END, values=row)
                        elif row: 
                             pm_message_var.set(f"Warning: Malformed row {i+2} in {PATIENTS_FILE}. Skipping.")
                             print(f"Warning: Malformed row {i+2} in {PATIENTS_FILE} with data {row}. Skipping.")
                    except IndexError: 
                        pm_message_var.set(f"Warning: Malformed row {i+2} (IndexError) in {PATIENTS_FILE}. Skipping.")
                        print(f"Warning: Malformed row {i+2} (IndexError) in {PATIENTS_FILE} with data {row}. Skipping.")
                    except csv.Error as e: 
                        pm_message_var.set(f"CSV parsing error at row {i+2} in {PATIENTS_FILE}: {e}. Skipping.")
                        print(f"CSV parsing error at row {i+2} in {PATIENTS_FILE}: {e}. Skipping.")
        except FileNotFoundError:
            pm_message_var.set(f"{PATIENTS_FILE} not found. A new file will be created.")
            initialize_patients_file() 
        except csv.Error as e: 
            pm_message_var.set(f"Error: {PATIENTS_FILE} is corrupted or unreadable: {e}")
            print(f"Error: {PATIENTS_FILE} is corrupted or unreadable: {e}")
        except Exception as e:
            pm_message_var.set(f"An unexpected error occurred while reading patients: {e}")
            print(f"An unexpected error occurred while reading patients: {e}")
        
        load_patient_name_cache()
        # Check if patient_selector_combo exists before trying to populate it
        # This is a bit of a hack for testing, ideally GUI elements are passed around or part of a class
        if 'patient_selector_combo' in locals() or 'patient_selector_combo' in globals():
            populate_patient_combobox()


    def add_patient():
        name = name_var.get()
        contact = contact_var.get().strip()
        address = address_var.get().strip()

        if not name:
            pm_message_var.set("Name field is required.")
            messagebox.showerror("Validation Error", "Name field is required.")
            return
        if not contact: 
            pm_message_var.set("Contact field is required.")
            messagebox.showerror("Validation Error", "Contact field is required.")
            return
        try: 
            patient_id = get_next_patient_id()
        except Exception as e:
            pm_message_var.set(f"Error generating patient ID: {e}")
            messagebox.showerror("Error", f"Could not generate patient ID: {e}")
            return
        new_patient = [str(patient_id), name, contact, address] 
        initialize_patients_file() 
        try:
            with open(PATIENTS_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_patient)
            name_var.set("")
            contact_var.set("")
            address_var.set("")
            pm_message_var.set("Patient added successfully!")
            messagebox.showinfo("Success", "Patient added successfully!")
            view_patients() 
        except Exception as e:
            pm_message_var.set(f"Error adding patient: {e}")
            messagebox.showerror("File Error", f"Error adding patient: {e}")

    def edit_patient():
        nonlocal selected_patient_id_for_edit
        if selected_patient_id_for_edit is None:
            messagebox.showerror("Selection Error", "Please select a patient from the list to edit.")
            return
        name = name_var.get()
        contact = contact_var.get().strip()
        address = address_var.get().strip()
        if not name:
            messagebox.showerror("Validation Error", "Name field cannot be empty.")
            return
        if not contact: 
            messagebox.showerror("Validation Error", "Contact field cannot be empty.")
            return
        try:
            initialize_patients_file()
            rows = []
            updated = False
            with open(PATIENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows.append(next(reader)) 
                for row in reader:
                    if row and row[0] == selected_patient_id_for_edit:
                        rows.append([selected_patient_id_for_edit, name, contact, address])
                        updated = True
                    else:
                        rows.append(row)
            if not updated:
                messagebox.showerror("Error", f"Patient ID {selected_patient_id_for_edit} not found for update.")
                return
            temp_file = PATIENTS_FILE + ".tmp"
            with open(temp_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            os.replace(temp_file, PATIENTS_FILE) 
            name_var.set("")
            contact_var.set("")
            address_var.set("")
            pm_message_var.set(f"Patient ID {selected_patient_id_for_edit} updated successfully!")
            messagebox.showinfo("Success", f"Patient ID {selected_patient_id_for_edit} updated successfully!")
            selected_patient_id_for_edit = None
            view_patients() 
        except Exception as e:
            pm_message_var.set(f"Error editing patient: {e}")
            messagebox.showerror("File Error", f"Error editing patient: {e}")

    def delete_patient():
        nonlocal selected_patient_id_for_edit
        selected_item = patient_tree.focus()
        if not selected_item:
             messagebox.showerror("Selection Error", "Please select a patient from the list to delete.")
             return
        patient_data = patient_tree.item(selected_item, "values")
        if not patient_data or len(patient_data) == 0: 
            messagebox.showerror("Selection Error", "Invalid patient selection.")
            return
        patient_id_to_delete = patient_data[0]
        if not messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete Patient ID {patient_id_to_delete}?"):
            return
        try:
            initialize_patients_file()
            rows = []
            deleted = False
            with open(PATIENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows.append(next(reader)) 
                for row in reader:
                    if row and row[0] == patient_id_to_delete:
                        deleted = True 
                    else:
                        rows.append(row)
            if not deleted: 
                messagebox.showerror("Error", f"Patient ID {patient_id_to_delete} not found for deletion.")
                return
            temp_file = PATIENTS_FILE + ".tmp"
            with open(temp_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            os.replace(temp_file, PATIENTS_FILE)
            pm_message_var.set(f"Patient ID {patient_id_to_delete} deleted successfully.")
            messagebox.showinfo("Success", f"Patient ID {patient_id_to_delete} deleted successfully.")
            if selected_patient_id_for_edit == patient_id_to_delete:
                name_var.set("")
                contact_var.set("")
                address_var.set("")
                selected_patient_id_for_edit = None
            view_patients() 
        except Exception as e:
            pm_message_var.set(f"Error deleting patient: {e}")
            messagebox.showerror("File Error", f"Error deleting patient: {e}")

    # --- Functions for Appointment Scheduling ---
    def populate_patient_combobox():
        nonlocal patient_combobox_map 
        patient_combobox_map.clear()
        patient_display_list = []
        for patient_id, name in patient_name_cache.items():
            display_string = f"{name} (ID: {patient_id})"
            patient_display_list.append(display_string)
            patient_combobox_map[display_string] = patient_id
        
        # Check if patient_selector_combo exists (it's a global variable in this scope)
        if 'patient_selector_combo' in locals() or 'patient_selector_combo' in globals():
            patient_selector_combo['values'] = patient_display_list
            if patient_display_list:
                current_selection = appointment_patient_var.get()
                if current_selection in patient_display_list:
                    patient_selector_combo.set(current_selection)
                else:
                    patient_selector_combo.current(0) 
            else:
                appointment_patient_var.set("") 
                patient_selector_combo['values'] = [] 
        else:
            pass # GUI element not ready

    def schedule_appointment():
        selected_patient_display = appointment_patient_var.get()
        patient_id = patient_combobox_map.get(selected_patient_display)
        date_val = appointment_date_var.get().strip()
        time_val = appointment_time_var.get().strip()
        reason_val = appointment_reason_var.get().strip()
        if not patient_id:
            as_message_var.set("Please select a patient.")
            messagebox.showerror("Validation Error", "Please select a patient.")
            return
        if not date_val: 
            as_message_var.set("Date is required.")
            messagebox.showerror("Validation Error", "Date is required (e.g., YYYY-MM-DD).")
            return
        if not time_val:
            as_message_var.set("Time is required.")
            messagebox.showerror("Validation Error", "Time is required (e.g., HH:MM).")
            return
        if not reason_val: 
            as_message_var.set("Reason for appointment is required.")
            messagebox.showerror("Validation Error", "Reason for appointment is required.")
            return
        try:
            from datetime import datetime 
            datetime.strptime(date_val, "%Y-%m-%d")
        except ValueError:
            as_message_var.set("Invalid Date format. Please use YYYY-MM-DD.")
            messagebox.showerror("Validation Error", "Invalid Date format. Please use YYYY-MM-DD.")
            return
        try:
            from datetime import datetime 
            datetime.strptime(time_val, "%H:%M")
        except ValueError:
            as_message_var.set("Invalid Time format. Please use HH:MM.")
            messagebox.showerror("Validation Error", "Invalid Time format. Please use HH:MM.")
            return
        try: 
            appointment_id = get_next_appointment_id()
        except Exception as e:
            as_message_var.set(f"Error generating appointment ID: {e}")
            messagebox.showerror("Error", f"Could not generate appointment ID: {e}")
            return
        new_appointment = [str(appointment_id), patient_id, date_val, time_val, reason_val]
        try:
            initialize_appointments_file()
            with open(APPOINTMENTS_FILE, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(new_appointment)
            appointment_date_var.set("")
            appointment_time_var.set("")
            appointment_reason_var.set("")
            as_message_var.set("Appointment scheduled successfully!")
            messagebox.showinfo("Success", "Appointment scheduled successfully!")
            view_appointments() 
        except Exception as e:
            as_message_var.set(f"Error scheduling appointment: {e}")
            messagebox.showerror("File Error", f"Error scheduling appointment: {e}")

    def view_appointments():
        # Check if GUI element exists before trying to use it (for testing)
        if not ('appointment_tree' in locals() or 'appointment_tree' in globals()):
            print("Debug: appointment_tree not found by view_appointments")
            return 

        for item in appointment_tree.get_children():
            appointment_tree.delete(item)
        load_patient_name_cache() 
        try:
            initialize_appointments_file()
            with open(APPOINTMENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                try:
                    header = next(reader)
                    if list(header) != APPOINTMENTS_HEADER:
                        as_message_var.set(f"Error: {APPOINTMENTS_FILE} header incorrect. Check file or delete to reset.")
                        return
                except StopIteration: 
                    as_message_var.set("No appointments found.")
                    return
                except csv.Error as e:
                    as_message_var.set(f"Error reading {APPOINTMENTS_FILE} header: {e}. File might be corrupted.")
                    return

                for i, row in enumerate(reader):
                    try:
                        if row and len(row) == len(APPOINTMENTS_HEADER):
                            patient_name = patient_name_cache.get(row[1], f"[Patient ID: {row[1]} - Name Not Found]")
                            display_row = [row[0], patient_name, row[1], row[2], row[3], row[4]]
                            appointment_tree.insert("", tk.END, values=display_row)
                        elif row: 
                            as_message_var.set(f"Warning: Malformed row {i+2} in {APPOINTMENTS_FILE}. Skipping.")
                            print(f"Warning: Malformed row {i+2} in {APPOINTMENTS_FILE} with data {row}. Skipping.")
                    except IndexError:
                         as_message_var.set(f"Warning: Malformed row {i+2} (IndexError) in {APPOINTMENTS_FILE}. Skipping.")
                         print(f"Warning: Malformed row {i+2} (IndexError) in {APPOINTMENTS_FILE} with data {row}. Skipping.")
                    except csv.Error as e:
                        as_message_var.set(f"CSV parsing error at row {i+2} in {APPOINTMENTS_FILE}: {e}. Skipping.")
                        print(f"CSV parsing error at row {i+2} in {APPOINTMENTS_FILE}: {e}. Skipping.")
        except FileNotFoundError:
            as_message_var.set(f"{APPOINTMENTS_FILE} not found. A new file will be created.")
            initialize_appointments_file()
        except csv.Error as e: 
            as_message_var.set(f"Error: {APPOINTMENTS_FILE} is corrupted or unreadable: {e}")
            print(f"Error: {APPOINTMENTS_FILE} is corrupted or unreadable: {e}")
        except Exception as e:
            as_message_var.set(f"An unexpected error occurred while reading appointments: {e}")
            print(f"An unexpected error occurred while reading appointments: {e}")

    def load_selected_appointment_to_form(event=None):
        nonlocal selected_appt_id_for_edit
        selected_item = appointment_tree.focus()
        if selected_item:
            appt_data = appointment_tree.item(selected_item, "values")
            if appt_data and len(appt_data) == len(APPOINTMENTS_HEADER) + 1: 
                selected_appt_id_for_edit = appt_data[0] 
                patient_id_of_selected_appt = appt_data[2] 
                patient_display_to_select = None
                for display_string, p_id in patient_combobox_map.items():
                    if p_id == patient_id_of_selected_appt:
                        patient_display_to_select = display_string
                        break
                if patient_display_to_select:
                    appointment_patient_var.set(patient_display_to_select)
                else:
                    appointment_patient_var.set("") 
                    as_message_var.set(f"Warning: Patient ID {patient_id_of_selected_appt} not found. Cannot edit patient for this appointment.")
                appointment_date_var.set(appt_data[3])    
                appointment_time_var.set(appt_data[4])    
                appointment_reason_var.set(appt_data[5])  
                as_message_var.set(f"Appointment ID {selected_appt_id_for_edit} loaded for editing.")
            else:
                as_message_var.set("Could not load appointment data. Selection invalid.")
                selected_appt_id_for_edit = None
        else:
            pass 

    def edit_appointment():
        nonlocal selected_appt_id_for_edit
        if selected_appt_id_for_edit is None:
            messagebox.showerror("Selection Error", "Please select an appointment from the list to edit.")
            return
        selected_patient_display = appointment_patient_var.get()
        patient_id = patient_combobox_map.get(selected_patient_display)
        date_val = appointment_date_var.get().strip()
        time_val = appointment_time_var.get().strip()
        reason_val = appointment_reason_var.get().strip()
        if not patient_id:
            as_message_var.set("Please select a patient.")
            messagebox.showerror("Validation Error", "Please select a patient.")
            return
        if not date_val:
            as_message_var.set("Date is required.")
            messagebox.showerror("Validation Error", "Date is required (e.g., YYYY-MM-DD).")
            return
        if not time_val:
            as_message_var.set("Time is required.")
            messagebox.showerror("Validation Error", "Time is required (e.g., HH:MM).")
            return
        if not reason_val: 
            as_message_var.set("Reason for appointment is required.")
            messagebox.showerror("Validation Error", "Reason for appointment is required.")
            return
        try:
            from datetime import datetime 
            datetime.strptime(date_val, "%Y-%m-%d")
        except ValueError:
            as_message_var.set("Invalid Date format. Please use YYYY-MM-DD.")
            messagebox.showerror("Validation Error", "Invalid Date format. Please use YYYY-MM-DD.")
            return
        try:
            from datetime import datetime 
            datetime.strptime(time_val, "%H:%M")
        except ValueError:
            as_message_var.set("Invalid Time format. Please use HH:MM.")
            messagebox.showerror("Validation Error", "Invalid Time format. Please use HH:MM.")
            return
        try:
            initialize_appointments_file()
            rows = []
            updated = False
            with open(APPOINTMENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows.append(next(reader)) 
                for row in reader:
                    if row and row[0] == selected_appt_id_for_edit: 
                        rows.append([selected_appt_id_for_edit, patient_id, date_val, time_val, reason_val])
                        updated = True
                    else:
                        rows.append(row)
            if not updated: 
                messagebox.showerror("Error", f"Appointment ID {selected_appt_id_for_edit} not found for update.")
                return
            temp_file = APPOINTMENTS_FILE + ".tmp"
            with open(temp_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            os.replace(temp_file, APPOINTMENTS_FILE)
            appointment_patient_var.set("") 
            appointment_date_var.set("")
            appointment_time_var.set("")
            appointment_reason_var.set("")
            as_message_var.set(f"Appointment ID {selected_appt_id_for_edit} updated successfully!")
            messagebox.showinfo("Success", f"Appointment ID {selected_appt_id_for_edit} updated successfully!")
            selected_appt_id_for_edit = None
            view_appointments()
        except Exception as e:
            as_message_var.set(f"Error editing appointment: {e}")
            messagebox.showerror("File Error", f"Error editing appointment: {e}")

    def cancel_appointment():
        nonlocal selected_appt_id_for_edit
        appt_id_to_cancel = None
        if selected_appt_id_for_edit:
            appt_id_to_cancel = selected_appt_id_for_edit
        else:
            selected_item = appointment_tree.focus()
            if not selected_item:
                messagebox.showerror("Selection Error", "Please select an appointment from the list to cancel.")
                return
            appt_data = appointment_tree.item(selected_item, "values")
            if not appt_data: 
                messagebox.showerror("Selection Error", "Invalid appointment selection.")
                return
            appt_id_to_cancel = appt_data[0] 
        if not messagebox.askyesno("Confirm Cancellation", f"Are you sure you want to cancel Appointment ID {appt_id_to_cancel}?"):
            return
        try:
            initialize_appointments_file()
            rows = []
            deleted = False
            with open(APPOINTMENTS_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                rows.append(next(reader)) 
                for row in reader:
                    if row and row[0] == appt_id_to_cancel:
                        deleted = True 
                    else:
                        rows.append(row)
            if not deleted: 
                messagebox.showerror("Error", f"Appointment ID {appt_id_to_cancel} not found for cancellation.")
                return
            temp_file = APPOINTMENTS_FILE + ".tmp"
            with open(temp_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            os.replace(temp_file, APPOINTMENTS_FILE)
            as_message_var.set(f"Appointment ID {appt_id_to_cancel} cancelled successfully.")
            messagebox.showinfo("Success", f"Appointment ID {appt_id_to_cancel} cancelled successfully.")
            if selected_appt_id_for_edit == appt_id_to_cancel:
                appointment_patient_var.set("")
                appointment_date_var.set("")
                appointment_time_var.set("")
                appointment_reason_var.set("")
                selected_appt_id_for_edit = None
            view_appointments()
        except Exception as e:
            as_message_var.set(f"Error cancelling appointment: {e}")
            messagebox.showerror("File Error", f"Error cancelling appointment: {e}")

    # --- Notebook Tab Change Handler ---
    def on_tab_changed(event):
        # Need to access notebook, defined later in this scope
        selected_tab_index = notebook.index(notebook.select())
        if selected_tab_index == 0: 
            view_patients() 
        elif selected_tab_index == 1: 
            load_patient_name_cache() 
            populate_patient_combobox()
            view_appointments()

    # --- GUI Setup ---
    notebook = ttk.Notebook(root)
    patient_management_frame = ttk.Frame(notebook)
    appointment_scheduling_frame = ttk.Frame(notebook)

    # --- Patient Management Tab GUI ---
    pm_controls_frame = ttk.LabelFrame(patient_management_frame, text="Add New Patient")
    pm_controls_frame.pack(padx=10, pady=10, fill="x")
    ttk.Label(pm_controls_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    name_entry = ttk.Entry(pm_controls_frame, textvariable=name_var, width=40)
    name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    ttk.Label(pm_controls_frame, text="Contact:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    contact_entry = ttk.Entry(pm_controls_frame, textvariable=contact_var, width=40)
    contact_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    ttk.Label(pm_controls_frame, text="Address:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    address_entry = ttk.Entry(pm_controls_frame, textvariable=address_var, width=40)
    address_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    pm_controls_frame.columnconfigure(1, weight=1) 
    add_button = ttk.Button(pm_controls_frame, text="Add Patient", command=add_patient)
    add_button.grid(row=3, column=0, padx=5, pady=10, sticky="ew")
    edit_button = ttk.Button(pm_controls_frame, text="Save Edit", command=edit_patient)
    edit_button.grid(row=3, column=1, padx=5, pady=10, sticky="ew")
    delete_button = ttk.Button(pm_controls_frame, text="Delete Selected", command=delete_patient)
    delete_button.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
    pm_controls_frame.grid_columnconfigure(0, weight=1)
    pm_controls_frame.grid_columnconfigure(1, weight=1)
    pm_view_frame = ttk.LabelFrame(patient_management_frame, text="Patient List")
    pm_view_frame.pack(padx=10, pady=10, fill="both", expand=True)
    view_button = ttk.Button(pm_view_frame, text="View/Refresh Patients", command=view_patients)
    view_button.pack(pady=5)
    pm_message_label = ttk.Label(pm_view_frame, textvariable=pm_message_var, relief=tk.SUNKEN) 
    pm_message_label.pack(fill="x", padx=5, pady=5)
    patient_appt_count_label = ttk.Label(pm_view_frame, textvariable=patient_appt_count_var)
    patient_appt_count_label.pack(fill="x", padx=5, pady=2, side=tk.BOTTOM) 
    columns = PATIENTS_HEADER
    patient_tree = ttk.Treeview(pm_view_frame, columns=columns, show="headings", selectmode="browse")
    for col in columns:
        patient_tree.heading(col, text=col)
        patient_tree.column(col, width=150, anchor=tk.W) 
    patient_tree.pack(fill="both", expand=True, padx=5, pady=5)
    patient_tree.bind("<<TreeviewSelect>>", load_selected_patient_to_form) 

    # --- Appointment Scheduling Tab GUI ---
    as_controls_frame = ttk.LabelFrame(appointment_scheduling_frame, text="Schedule New Appointment")
    as_controls_frame.pack(padx=10, pady=10, fill="x")
    ttk.Label(as_controls_frame, text="Select Patient:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    patient_selector_combo = ttk.Combobox(as_controls_frame, textvariable=appointment_patient_var, state="readonly", width=37)
    patient_selector_combo.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    ttk.Label(as_controls_frame, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    date_entry = ttk.Entry(as_controls_frame, textvariable=appointment_date_var, width=40)
    date_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
    ttk.Label(as_controls_frame, text="Time (HH:MM):").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    time_entry = ttk.Entry(as_controls_frame, textvariable=appointment_time_var, width=40)
    time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
    ttk.Label(as_controls_frame, text="Reason:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    reason_entry = ttk.Entry(as_controls_frame, textvariable=appointment_reason_var, width=40)
    reason_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
    as_controls_frame.columnconfigure(1, weight=1)
    schedule_button = ttk.Button(as_controls_frame, text="Schedule Appointment", command=schedule_appointment)
    schedule_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")
    edit_appointment_button = ttk.Button(as_controls_frame, text="Save Appointment Edit", command=edit_appointment)
    edit_appointment_button.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
    cancel_appointment_button = ttk.Button(as_controls_frame, text="Cancel Selected Appointment", command=cancel_appointment)
    cancel_appointment_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
    as_controls_frame.grid_columnconfigure(0, weight=1)
    as_controls_frame.grid_columnconfigure(1, weight=1)
    as_view_frame = ttk.LabelFrame(appointment_scheduling_frame, text="Appointment List")
    as_view_frame.pack(padx=10, pady=10, fill="both", expand=True)
    as_view_button = ttk.Button(as_view_frame, text="View/Refresh Appointments", command=view_appointments)
    as_view_button.pack(pady=5)
    as_message_label = ttk.Label(as_view_frame, textvariable=as_message_var, relief=tk.SUNKEN)
    as_message_label.pack(fill="x", padx=5, pady=5)
    appointment_columns = ["AppID", "Patient Name", "PatientID", "Date", "Time", "Reason"]
    appointment_tree = ttk.Treeview(as_view_frame, columns=appointment_columns, show="headings", selectmode="browse") 
    appointment_tree.bind("<<TreeviewSelect>>", load_selected_appointment_to_form) 
    for col_name in appointment_columns:
        width = 100
        anchor = tk.W
        if col_name == "Patient Name": width = 150
        elif col_name == "Reason": width = 200
        elif col_name == "PatientID": width = 0 
        appointment_tree.heading(col_name, text=col_name)
        if width == 0: 
             appointment_tree.column(col_name, width=width, stretch=tk.NO)
        else:
            appointment_tree.column(col_name, width=width, anchor=anchor)
    appointment_tree.pack(fill="both", expand=True, padx=5, pady=5)

    notebook.add(patient_management_frame, text="Patient Management")
    notebook.add(appointment_scheduling_frame, text="Appointment Scheduling")
    notebook.pack(expand=True, fill="both", padx=10, pady=10)
    notebook.bind("<<NotebookTabChanged>>", on_tab_changed) # Moved bind after notebook is packed
    
    root.minsize(750, 550) 
    initialize_patients_file()
    initialize_appointments_file()
    load_patient_name_cache() 
    
    # Manually trigger population for the initially selected tab
    # Ensure GUI elements like patient_tree are created before view_patients is called
    # The Treeviews and other widgets are now defined before this block
    current_tab_index = notebook.index(notebook.select())
    if current_tab_index == 0:
        view_patients() 
    elif current_tab_index == 1:
        populate_patient_combobox() 
        view_appointments()
    
    root.mainloop()

if __name__ == "__main__":
    main_gui_app()
