# CrimsonCode2026
This is for the WSU Crimson Code Hackathon 2026, the theme being "Reinventing the Wheel"

Created by: Roagan Wolf, Blake Watson, Brock Childers, Daniel Aldrich

The goal of this project is to make a calculator that allows you to choose 
the complexity of your response, as well as keeping tabs for multiple 
calculations.For example, if I am doing an algebraic problem and just want 
the direct answer, I can get that. However, if I am doing an integral and 
need to just find the u sub, I can get that. While all of this is
happening, I can keep track of all calculations across the tabs.

In the end, the idea is to have Python calculate the solutions for the
expressions/equations, while having the Gemini LLM make the framework for
the explanation of the steps with the Python solutions being plugged into
the framework.

As of February 22nd, 2026:
- The calculator has not implemented the LLM function
- Simply doing algebraic expressions and equations. (one variable = x)
- There are functions/buttons on the frontend that are present but not
  implemented. There is no direct way of knowing which ones work except
  by clicking them, which will input nothing if done so.
- Tabs backend is not connected with frontend. Functionality of
  backend should be close to done.
- UI is still a major WIP. 

How to test:
1. Run the following terminal commands
    * python -m venv venv
    * venv\Scripts\activate
    * pip install -r requirements.txt
    * uvicorn app.main:app --reload

2. Run the html file inside of frontend
