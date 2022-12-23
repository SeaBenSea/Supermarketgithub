"""
    Stage: Development-01
    @author: Ayhan Emre Sermet - 117202098
    @author: Yagiz Uygun - 119202075
    @author: Ata Aral Candar - 120202044

    stage: Devolopment -02:
    @author: Mohammad Hamed - 120200155
    @author: ömercan topalömer - 120202103
    @author: MERT MENGİLLİ -119202055

    Stage : Code Review
    @author: Deniz Gunenc - 120200078
    @Huseyin Enes Tandogan - 119200040
"""

import tkinter as tk

# Test username and passwords
test_login_username = 'test_username'
test_login_password = 'test_pass'


class newWindow:
    def __init__(self):
        self.window = tk.Tk()
        self._initializeGUI()
        self._addGUIElementsToFrame()


# gui initilizer


    def _initializeGUI(self):
        # add and iptal buttons
        # text based entry list
        self.btn01 = tk.Button(text="add")
        self.btn02 = tk.Button(text="iptal")
        self.txt01 = tk.Entry()

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-2>", self.handle_click)

    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """

    def _addGUIElementsToFrame(self):
        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)

    def _additems(self):
        pass


class LoginWindow:
    # constructor
    def __init__(self):
        self.window = tk.Tk()

        self._initializeGUI()
        self._addGUIElementsToFrame()

        # start the GUI frame
        self.window.mainloop()

    """
        Initialize GUI elements. If it is necessary, you can add
        more elements.

        ! PLEASE RENAME THE OBJECTS ACCORDING TO THEIR PURPOSES !
        ! YOU CAN ADD MORE ELEMENTS IF IT IS NECESSARY !
    """

    def _initializeGUI(self):
        self.lbl01 = tk.Label(text="Kullanici adi ")
        self.lbl02 = tk.Label(text="sifre")

        self.txt01 = tk.Entry()
        self.txt02 = tk.Entry()

        self.btn01 = tk.Button(text="Onayla")
        self.btn02 = tk.Button(text="iptal")

        self.btn01.bind("<Button-1>", self.handle_click)
        self.btn02.bind("<Button-2>", self.handle_click)

        def create_supermarket_window(self):
            self.after_login_window = tk.Tk()
            self.after_login_window.geometry("720x576")
            self.after_login_window.title('Supermarket')

    def validate_and_login_user(self, event):
        username = self.txt01.get()
        password = self.txt02.get()
        if (username == "admin" and password == "admin"):
            # After a successful login, we create a new 'page' or a window to show the supermarket.
            print("login success")
            # self.create_supermarket_window()
            # Login window can now be destroyed
            self.window.destroy()
            # Start the after login window main loop
            # self.after_login_window.mainloop()
            # creating new page
            self.createNewPage()

    """
        Add GUI elements to the layout of the frame. If it is necessary,
        you can add more elements.
    """

    def _addGUIElementsToFrame(self):
        self.lbl01.grid(row=0, column=0, padx=10, pady=5)
        self.txt01.grid(row=0, column=1, padx=10, pady=5)

        self.lbl02.grid(row=1, column=0, padx=10, pady=5)
        self.txt02.grid(row=1, column=1, padx=10, pady=5)

        self.btn01.grid(row=2, column=0, padx=10, pady=5)
        self.btn02.grid(row=2, column=1, padx=10, pady=5)

    """
        Action listener for the buttons. If "event.widget" is from
        one of the buttons, apply the related operation.

        :param event: action event for detecting which button is clicked
    """
    # function to handle button pressing for clicking

    def handle_click(self, event):
        if (self.btn01):
            self.validate_and_login_user(event)
            print("welocme")

        pass

    # function to create a new window:
    def createNewPage(self):
        newWindow()


# main method for testing the application
if __name__ == "__main__":
    LoginWindow()
