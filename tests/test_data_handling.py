import unittest
import os
import sys
from unittest.mock import MagicMock

# --- Mocking Tkinter before importing main ---
# Create a mock object for the tkinter module
mock_tkinter = MagicMock()
sys.modules['tkinter'] = mock_tkinter
sys.modules['tkinter.ttk'] = MagicMock() # Mock ttk as well if it's imported directly
sys.modules['tkinter.messagebox'] = MagicMock() # Mock messagebox

# Now that tkinter is mocked, we can import main and its components
import csv
import tempfile
from unittest.mock import patch
import shutil

# Add the parent directory to sys.path to allow direct import of main
# import sys # Already imported above
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now import functions from main.py
# We need to be careful as main.py also runs a Tkinter app if __name__ == "__main__"
# We will only import specific functions/variables we need.
from main import (
    initialize_patients_file, get_next_patient_id, PATIENTS_HEADER, PATIENTS_FILE,
    initialize_appointments_file, get_next_appointment_id, APPOINTMENTS_HEADER, APPOINTMENTS_FILE
    # We will simulate add/edit/delete logic by direct CSV manipulation in tests for now
    # as the main functions are too coupled with Tkinter.
)

class TestPatientDataHandling(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        # Create a temporary file path for patients
        self.temp_patients_file = os.path.join(self.test_dir, "test_patients.csv")
        # Patch the global PATIENTS_FILE path in main.py
        self.patients_file_patcher = patch('main.PATIENTS_FILE', self.temp_patients_file)
        self.patients_file_patcher.start()

    def tearDown(self):
        # Stop the patcher
        self.patients_file_patcher.stop()
        # Remove the temporary directory and its contents
        shutil.rmtree(self.test_dir)

    def test_initialize_new_patients_file(self):
        self.assertFalse(os.path.exists(self.temp_patients_file))
        initialize_patients_file()
        self.assertTrue(os.path.exists(self.temp_patients_file))
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, PATIENTS_HEADER)
            with self.assertRaises(StopIteration): # Should be empty after header
                next(reader)
    
    def test_initialize_existing_empty_patients_file(self):
        # Create an empty file
        open(self.temp_patients_file, 'w').close()
        self.assertTrue(os.path.exists(self.temp_patients_file))
        self.assertEqual(os.path.getsize(self.temp_patients_file), 0)
        
        initialize_patients_file()
        self.assertTrue(os.path.exists(self.temp_patients_file))
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, PATIENTS_HEADER)
            with self.assertRaises(StopIteration):
                next(reader)

    def test_get_next_patient_id_empty_file(self):
        initialize_patients_file() # Ensure header is there
        next_id = get_next_patient_id()
        self.assertEqual(next_id, 1)

    def test_get_next_patient_id_with_data(self):
        initialize_patients_file()
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Test User", "12345", "Test Address"])
            writer.writerow(["2", "Another User", "67890", "Another Address"])
        next_id = get_next_patient_id()
        self.assertEqual(next_id, 3)

    def test_get_next_patient_id_non_sequential(self):
        initialize_patients_file()
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["5", "Test User", "12345", "Test Address"])
        next_id = get_next_patient_id()
        self.assertEqual(next_id, 6)

    def test_get_next_patient_id_file_with_only_header(self):
        initialize_patients_file() 
        # File only has header from initialize_patients_file
        next_id = get_next_patient_id()
        self.assertEqual(next_id, 1)

    def test_get_next_patient_id_malformed_id(self):
        initialize_patients_file()
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Test User", "123", "Addr1"])
            writer.writerow(["NotANumber", "User 2", "456", "Addr2"])
            writer.writerow(["3", "User 3", "789", "Addr3"])
        next_id = get_next_patient_id()
        self.assertEqual(next_id, 4) # Should skip "NotANumber" and find 3 as max

class TestAppointmentDataHandling(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.temp_appointments_file = os.path.join(self.test_dir, "test_appointments.csv")
        self.appointments_file_patcher = patch('main.APPOINTMENTS_FILE', self.temp_appointments_file)
        self.appointments_file_patcher.start()

        # Appointments need a patient file for some context (though not directly used by init/getID)
        self.temp_patients_file = os.path.join(self.test_dir, "test_patients.csv")
        self.patients_file_patcher = patch('main.PATIENTS_FILE', self.temp_patients_file)
        self.patients_file_patcher.start()
        # Initialize a dummy patient file for appointment tests that might interact with patient data
        initialize_patients_file() 


    def tearDown(self):
        self.appointments_file_patcher.stop()
        self.patients_file_patcher.stop()
        shutil.rmtree(self.test_dir)

    def test_initialize_new_appointments_file(self):
        self.assertFalse(os.path.exists(self.temp_appointments_file))
        initialize_appointments_file()
        self.assertTrue(os.path.exists(self.temp_appointments_file))
        with open(self.temp_appointments_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, APPOINTMENTS_HEADER)
            with self.assertRaises(StopIteration):
                next(reader)

    def test_get_next_appointment_id_empty_file(self):
        initialize_appointments_file()
        next_id = get_next_appointment_id()
        self.assertEqual(next_id, 1)

    def test_get_next_appointment_id_with_data(self):
        initialize_appointments_file()
        with open(self.temp_appointments_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "1", "2023-01-01", "10:00", "Checkup"])
            writer.writerow(["2", "2", "2023-01-02", "11:00", "Follow-up"])
        next_id = get_next_appointment_id()
        self.assertEqual(next_id, 3)

# To simulate data operations (add, edit, delete) without refactoring main.py's Tkinter parts,
# we can write helper functions here that directly manipulate the CSV files using the patched paths.
# Then, we can assert the state of the CSV.

# Example of how we might test "add patient" logic by directly manipulating CSV:
# This is NOT testing main.add_patient directly, but the underlying data handling principle.
    def test_simulated_add_patient(self):
        initialize_patients_file() # Creates file with header

        # Simulate getting next ID (already tested in get_next_patient_id)
        patient_id = "1" 
        name = "Test Patient"
        contact = "111-222-3333"
        address = "123 Test St"
        
        # Logic similar to what add_patient would do with CSV
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([patient_id, name, contact, address])

        # Verify by reading
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader) # Skip header
            self.assertEqual(header, PATIENTS_HEADER)
            data_row = next(reader)
            self.assertEqual(data_row, [patient_id, name, contact, address])
            with self.assertRaises(StopIteration): # No more data
                next(reader)

    def test_simulated_delete_patient(self):
        initialize_patients_file()
        # Add some initial data
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Patient One", "123", "Addr1"])
            writer.writerow(["2", "Patient Two", "456", "Addr2"]) # This one to delete
            writer.writerow(["3", "Patient Three", "789", "Addr3"])
        
        patient_id_to_delete = "2"
        
        # Logic similar to what delete_patient would do
        rows = []
        deleted = False
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows.append(next(reader)) # Keep header
            for row in reader:
                if row and row[0] == patient_id_to_delete:
                    deleted = True
                else:
                    rows.append(row)
        self.assertTrue(deleted)

        with open(self.temp_patients_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Verify
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            remaining_ids = [row[0] for row in reader if row]
            self.assertEqual(remaining_ids, ["1", "3"])
    
    def test_simulated_edit_patient(self):
        initialize_patients_file()
        # Add initial data
        initial_data = [
            PATIENTS_HEADER,
            ["1", "Old Name", "Old Contact", "Old Address"],
            ["2", "Other Patient", "Other Contact", "Other Address"]
        ]
        with open(self.temp_patients_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(initial_data)

        patient_id_to_edit = "1"
        updated_name = "New Name"
        updated_contact = "New Contact"
        updated_address = "New Address"

        # Logic similar to edit_patient
        rows = []
        updated = False
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows.append(next(reader)) # Keep header
            for row in reader:
                if row and row[0] == patient_id_to_edit:
                    rows.append([patient_id_to_edit, updated_name, updated_contact, updated_address])
                    updated = True
                else:
                    rows.append(row)
        self.assertTrue(updated)

        with open(self.temp_patients_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        # Verify
        with open(self.temp_patients_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            edited_row = None
            for row in reader:
                if row and row[0] == patient_id_to_edit:
                    edited_row = row
                    break
            self.assertIsNotNone(edited_row)
            self.assertEqual(edited_row, [patient_id_to_edit, updated_name, updated_contact, updated_address])

class TestAppointmentDataHandling(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.temp_appointments_file = os.path.join(self.test_dir, "test_appointments.csv")
        self.appointments_file_patcher = patch('main.APPOINTMENTS_FILE', self.temp_appointments_file)
        self.appointments_file_patcher.start()

        # Appointments need a patient file for some context
        self.temp_patients_file = os.path.join(self.test_dir, "test_patients.csv")
        self.patients_file_patcher = patch('main.PATIENTS_FILE', self.temp_patients_file)
        self.mock_patients_file = self.patients_file_patcher.start()
        
        # Initialize a dummy patient file for appointment tests
        initialize_patients_file() 
        # Add some dummy patients to self.temp_patients_file for appointment context
        with open(self.temp_patients_file, mode='a', newline='') as pf:
            p_writer = csv.writer(pf)
            p_writer.writerow(["1", "Patient Alpha", "111", "Addr A"])
            p_writer.writerow(["2", "Patient Beta", "222", "Addr B"])


    def tearDown(self):
        self.appointments_file_patcher.stop()
        self.patients_file_patcher.stop()
        shutil.rmtree(self.test_dir)

    def test_initialize_new_appointments_file(self):
        self.assertFalse(os.path.exists(self.temp_appointments_file))
        initialize_appointments_file()
        self.assertTrue(os.path.exists(self.temp_appointments_file))
        with open(self.temp_appointments_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, APPOINTMENTS_HEADER)
            with self.assertRaises(StopIteration):
                next(reader)

    def test_get_next_appointment_id_empty_file(self):
        initialize_appointments_file()
        next_id = get_next_appointment_id()
        self.assertEqual(next_id, 1)

    def test_get_next_appointment_id_with_data(self):
        initialize_appointments_file()
        with open(self.temp_appointments_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "1", "2023-01-01", "10:00", "Checkup"])
            writer.writerow(["2", "2", "2023-01-02", "11:00", "Follow-up"])
        next_id = get_next_appointment_id()
        self.assertEqual(next_id, 3)

    def test_simulated_schedule_appointment(self):
        initialize_appointments_file()
        
        appt_id = "1"
        patient_id = "1" # Assumes patient "1" exists from setUp
        date = "2024-03-10"
        time = "14:00"
        reason = "Annual Checkup"

        with open(self.temp_appointments_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([appt_id, patient_id, date, time, reason])

        with open(self.temp_appointments_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            data_row = next(reader)
            self.assertEqual(data_row, [appt_id, patient_id, date, time, reason])

    def test_simulated_cancel_appointment(self):
        initialize_appointments_file()
        initial_appts = [
            APPOINTMENTS_HEADER,
            ["1", "1", "2024-01-01", "10:00", "Reason A"],
            ["2", "2", "2024-01-02", "11:00", "Reason B"], # To cancel
            ["3", "1", "2024-01-03", "12:00", "Reason C"]
        ]
        with open(self.temp_appointments_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(initial_appts)

        appt_id_to_cancel = "2"
        rows = []
        cancelled = False
        with open(self.temp_appointments_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows.append(next(reader)) # header
            for row in reader:
                if row and row[0] == appt_id_to_cancel:
                    cancelled = True
                else:
                    rows.append(row)
        self.assertTrue(cancelled)

        with open(self.temp_appointments_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        with open(self.temp_appointments_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader) # Skip header
            remaining_ids = [row[0] for row in reader if row]
            self.assertEqual(remaining_ids, ["1", "3"])

# --- Tests for other helper functions ---
from main import load_patient_name_cache, patient_name_cache, update_patient_appointment_count

class TestHelperFunctions(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.temp_patients_file = os.path.join(self.test_dir, "test_patients.csv")
        self.temp_appointments_file = os.path.join(self.test_dir, "test_appointments.csv")

        self.patients_file_patcher = patch('main.PATIENTS_FILE', self.temp_patients_file)
        self.appointments_file_patcher = patch('main.APPOINTMENTS_FILE', self.temp_appointments_file)
        
        self.mock_patients_file = self.patients_file_patcher.start()
        self.mock_appointments_file = self.appointments_file_patcher.start()
        
        # Clear the global cache before each test
        patient_name_cache.clear()


    def tearDown(self):
        self.patients_file_patcher.stop()
        self.appointments_file_patcher.stop()
        shutil.rmtree(self.test_dir)

    def test_load_patient_name_cache_empty_file(self):
        initialize_patients_file() # Creates header
        load_patient_name_cache()
        self.assertEqual(patient_name_cache, {})

    def test_load_patient_name_cache_with_data(self):
        initialize_patients_file()
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Alice", "123", "Wonderland"])
            writer.writerow(["2", "Bob", "456", "Builderland"])
        
        load_patient_name_cache()
        expected_cache = {"1": "Alice", "2": "Bob"}
        self.assertEqual(patient_name_cache, expected_cache)

    def test_load_patient_name_cache_malformed_row(self):
        initialize_patients_file()
        with open(self.temp_patients_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "Alice", "123", "Wonderland"])
            writer.writerow(["2"]) # Malformed row
            writer.writerow(["3", "Charlie", "789", "Candyland"])
        
        load_patient_name_cache()
        expected_cache = {"1": "Alice", "3": "Charlie"} # Should skip the malformed row
        self.assertEqual(patient_name_cache, expected_cache)

    def test_update_patient_appointment_count_no_appointments_file(self):
        # PATIENTS_FILE is mocked and can exist or not, doesn't matter for this specific test part
        # APPOINTMENTS_FILE is mocked, and we ensure it does not exist
        if os.path.exists(self.temp_appointments_file):
            os.remove(self.temp_appointments_file) # Ensure it's gone

        # Create a MagicMock instance to simulate a Tkinter StringVar
        mock_string_var = MagicMock()
        update_patient_appointment_count("1", mock_string_var)
        mock_string_var.set.assert_called_once_with("Appointments: 0")

    def test_update_patient_appointment_count_empty_appointments_file(self):
        initialize_appointments_file() # Creates header
        mock_string_var = MagicMock()
        update_patient_appointment_count("1", mock_string_var)
        mock_string_var.set.assert_called_once_with("Appointments: 0")

    def test_update_patient_appointment_count_with_data(self):
        initialize_appointments_file()
        with open(self.temp_appointments_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["1", "1", "2023-01-01", "10:00", "Reason A"]) # Patient 1
            writer.writerow(["2", "2", "2023-01-02", "11:00", "Reason B"]) # Patient 2
            writer.writerow(["3", "1", "2023-01-03", "12:00", "Reason C"]) # Patient 1
        
        mock_string_var_p1 = MagicMock()
        update_patient_appointment_count("1", mock_string_var_p1)
        mock_string_var_p1.set.assert_called_with("Appointments: 2")
        
        mock_string_var_p2 = MagicMock()
        update_patient_appointment_count("2", mock_string_var_p2)
        mock_string_var_p2.set.assert_called_with("Appointments: 1")

        mock_string_var_p3 = MagicMock()
        update_patient_appointment_count("3", mock_string_var_p3) # Non-existent patient
        mock_string_var_p3.set.assert_called_with("Appointments: 0")

# --- Date/Time Validation Tests (Conceptual) ---
# Since date/time validation is inside Tkinter-coupled functions,
# we'll test the validation logic conceptually.
# We can create a helper in the test or directly use datetime.strptime

from datetime import datetime

class TestValidationLogic(unittest.TestCase):
    def test_date_format_valid(self):
        try:
            datetime.strptime("2024-03-10", "%Y-%m-%d")
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid)

    def test_date_format_invalid_letters(self):
        with self.assertRaises(ValueError):
            datetime.strptime("2024-MM-DD", "%Y-%m-%d")

    def test_date_format_invalid_format(self):
        with self.assertRaises(ValueError):
            datetime.strptime("10/03/2024", "%Y-%m-%d")

    def test_time_format_valid(self):
        try:
            datetime.strptime("14:30", "%H:%M")
            valid = True
        except ValueError:
            valid = False
        self.assertTrue(valid)

    def test_time_format_invalid_letters(self):
        with self.assertRaises(ValueError):
            datetime.strptime("HH:MM", "%H:%M")

    def test_time_format_invalid_range(self): # strptime checks for valid time values
         with self.assertRaises(ValueError):
            datetime.strptime("25:00", "%H:%M")


if __name__ == '__main__':
    # This allows running tests directly from this file
    # It will also run if you use `python -m unittest discover tests`
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
