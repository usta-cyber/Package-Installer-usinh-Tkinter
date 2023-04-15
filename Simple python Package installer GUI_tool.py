import tkinter as tk
import subprocess

class PackageInstaller:
    def __init__(self, master):
        self.master = master
        self.master.title("Python Package Installer")

        self.packages_label = tk.Label(self.master, text="Enter package names (separated by space):")
        self.packages_label.pack()

        self.packages_entry = tk.Entry(self.master)
        self.packages_entry.pack()

        self.install_button = tk.Button(self.master, text="Install Packages", command=self.install_packages)
        self.install_button.pack()

        self.installed_label = tk.Label(self.master, text="Installed Packages:")
        self.installed_label.pack()

        self.installed_text = tk.Text(self.master)
        self.installed_text.pack()

    def install_packages(self):
        packages = self.packages_entry.get().split()
        for package in packages:
            subprocess.call(['pip', 'install', package])
        self.show_installed_packages()

    def show_installed_packages(self):
        installed_packages = subprocess.check_output(['pip', 'list']).decode('utf-8')
        self.installed_text.delete('1.0', tk.END)
        self.installed_text.insert(tk.END, installed_packages)

if __name__ == '__main__':
    root = tk.Tk()
    app = PackageInstaller(root)
    root.mainloop()
