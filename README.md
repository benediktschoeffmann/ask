# Ask

I wrote this little program to familiarize myself with working with "AI" and python.

Enter your GROQ-ApiKey into the `.env`-file and run:

```bash
python3 ask.py
```

The program will ask you to enter a question, which it then tries to answer.

The textual Answer will be printed to the screen, in addition, 2 files named the slug of the question string will be created.

- a json file, with meta data about the query in json format
- a md file, where the text is saved in md format

These files lie in the `questions/`-folder.
