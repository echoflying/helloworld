import streamlit as st

# global environment store into st.session_state
# set a easy way to access
class Env():
    # save all your variables inside st.session_state
    def __init__(self):
        if not self.has("working_step"):
            st.session_state.working_step = 1
        if not self.has("show"):
            st.session_state.show = Show()
        if not self.has("app"):
            st.session_state.app = App()
 
    def __getattr__(self, key):
        if key not in st.session_state:
            raise AttributeError(f"Invalid access to st.session_state, key = {key}")
        else:
            return st.session_state[key]

    def __setattr__(self, key, value):
        st.session_state[key] = value

    def __getitem__(self, key):
        if key not in st.session_state:
            raise AttributeError(f"Invalid access to st.session_state, key = {key}")
        else:
            return st.session_state[key]

    def __setitem__(self, key, value):
        st.session_state[key] = value

    def __len__(self, key):
        return len(st.session_state[key])

    def has(self, key):
        if key not in st.session_state:
            return False
        else:
            return True
        

# manage all layout
class Show():
    show_app_header = None
    show_hello = None 
    def __init__(self):
        self.show_app_header = st.empty()
        self.show_hello = st.empty()

    def run(self):
        self.show_app_header.header("Hello world ...")

        if env.working_step == 1:
            self.show_step1()
        elif env.working_step == 2:
            self.show_step2()
        else:
            raise ValueError(f"{self.working_step}")

    def show_step1(self):
        self.show_hello.empty()
        cav = self.show_hello.container(border = True)
        cav.write("Step 1")
        text = cav.text_input(label = "What's your name?", 
                              value="", 
                              on_change =env.app.on_change_name_input)
        # other way to pass the input value is by st.session_state.key_str, which break the way we encapsulate the environment
        
        if text:
            env.app.set_name(text)
        cav.button("Go Next step", on_click=env.app.on_click1)

    def show_step2(self):
        self.show_hello.empty()
        cav = self.show_hello.container(border = True)
        cav.write("Step 2")
        cav.write("Hello, " + env.app.get_name())
        cav.button("Finish, we go back step 1", on_click=env.app.on_click2)

class App():
    hello_message2 = ""
    name = ""
    show_name = ""

    def set_name(self, s):
        self.name = s

    def get_name(self):
        return self.show_name

    def on_change_name_input(self):
        pass
        
    def on_click1(self):
        # your business logic here
        if self.name == "":
            self.show_name = "Stranger"
        else:
            self.show_name = self.name

        # goto next step 
        env.working_step = 2
    
    def on_click2(self):
        # your business logic here
        self.name = ""

        # goto other step, here we back step 1.
        env.working_step = 1

# start the program
env = Env()
env.show.run()
