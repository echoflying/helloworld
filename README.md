This small app try to demo a application framework for streamlit.

### Basic idea:
1. Separate the layout and logic.
2. Use application states to control the layout since Streamlit will run the code repeatedly.
   - `working_step` is used

### Class Definitions
1. class Env: used to access global variables st.session_state, make access the variable more readable
2. class Show: manage all layout
3. class App: implement all business logic

### Two strategies to connect Show and App:
1. through global variables, Env
2. use instance, app in Show and show in App, which will combine two classes
   - direct access variable in eather class, or 
   - use method call to encapsulate the detail

we use 2nd method in the demo code.

### Note:
- The "default way" Streamlit use to connect input widgets to st.session_state via "keywords" is a BAD concept.
  Hide in another global session variable and pass to on_change args is better.


