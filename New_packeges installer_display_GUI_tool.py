import tkinter as tk
import subprocess

class PackageInstaller:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Package Installer")

        self.GUI_label = tk.Label(self.master, text="Python Package Installer", fg="Green",font=("Arial", 16,"bold"))
        self.GUI_label.pack(pady=10)

 
        # Frame for package installation
        self.install_frame = tk.Frame(self.master)
        self.install_frame.pack(pady=10)

        # Label for package installation
        self.install_label = tk.Label(self.install_frame, text="Enter package names (separated by new line):", fg="blue",font=("Arial", 12,"bold"))
        self.install_label.grid(row=0, column=0, sticky=tk.W)

        # Text box for package installation
        self.install_text = tk.Text(self.install_frame, height=10, width=50)
        self.install_text.grid(row=1, column=0, padx=10)

        # Button for package installation
        self.install_button = tk.Button(self.install_frame, text="Install Packages", command=self.install_packages, fg="red")
        self.install_button.grid(row=1, column=1, padx=10)

        # Frame for package list
        self.list_frame = tk.Frame(self.master)
        self.list_frame.pack(pady=10)

        # Button for package list
        self.list_button = tk.Button(self.list_frame, text="Display Installed Packages", command=self.show_installed_packages, fg="green")
        self.list_button.pack()

        # Text box for package list
        self.list_text = tk.Text(self.list_frame, height=10, width=50, bg="lightgray")
        self.list_text.pack(pady=10)

        # Button for package deletion
        self.delete_button = tk.Button(self.list_frame, text="Delete Selected Package", command=self.delete_package, fg="red")
        self.delete_button.pack()

        # Text box for package deletion
        self.delete_text = tk.Text(self.list_frame, height=1, width=50, bg="lightgray")
        self.delete_text.pack(pady=10)

    def install_packages(self):
        # Get package names from text box
        packages = self.install_text.get('1.0', tk.END).split()

        # Install packages
        for package in packages:
            try:
                subprocess.check_call(['pip', 'install', package])
            except subprocess.CalledProcessError as e:
                self.delete_text.delete('1.0', tk.END)
                self.delete_text.insert(tk.END, "Error installing package: {}".format(package))
                self.delete_text.insert(tk.END, "\n" + e.output.decode())
                break

        # Show installed packages
        self.show_installed_packages()

    def show_installed_packages(self):
        # Get installed packages
        installed_packages = subprocess.check_output(['pip', 'list', '--format=columns']).decode('utf-8')

        # Show installed packages in text box
        self.list_text.delete('1.0', tk.END)
        self.list_text.insert(tk.END, installed_packages)

    def delete_package(self):
        # Get selected package
        package = self.list_text.get('sel.first', 'sel.last').split()[0]

        # Delete package
        try:
            subprocess.check_call(['pip', 'uninstall', '-y', package])
            self.delete_text.delete('1.0', tk.END)
            self.delete_text.insert(tk.END, "Package {} deleted successfully".format(package))
        except subprocess.CalledProcessError as e:
            self.delete_text.delete('1.0', tk.END)
            self.delete_text.insert(tk.END, "Error deleting package: {}".format(package))
            self.delete_text.insert(tk.END, "\n" + e.output.decode())

        # Show installed packages
        self.show_installed_packages


if __name__ == '__main__':
    root = tk.Tk()
    app = PackageInstaller(root)
    root.mainloop()
