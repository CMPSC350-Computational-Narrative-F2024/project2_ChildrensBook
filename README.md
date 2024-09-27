# Project 2: Generated Children's Book

## Timeline

Activity                   | Deadline
-------------------------- | ------------------------------
Regular Commits:  | September 26th-October 18th, 2024 (total: 20 commit requirement, at least 1 on September 27th and October 4th)
Planning (add a age range and theme to the report) | September 26th, 2024 by 4:20pm
Peer Interview ([Google Form](https://forms.gle/R7wzwzshncjcyjdf9)) | October 4th, 2024 during lab
Final submission and Critique | October 18th, 2024 by 11am, critique in class and during lab if needed

## Summary

In our work so far, we have established and broken apart our understanding of the ways in which meaning occurs in a generative text. We have explored using language as a kind of symbol and are starting to investigate the effects of grammar.

In this project, you are invited to create a children's book. Of course, all aspects of this book must be automatically generated. Your craft comes in our skill of "prompt engineering" while employing both theoretical and technical skills that we have been investigating.  Be _creative_ and _weird_! 

## Learning

* [Methods of Prompt Programming](https://www.promptingguide.ai/techniques)
* [OpenAI API](https://platform.openai.com/docs/overview)
* [OpenAI Notes on prompt design](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)

## Learning Outcomes

* Learn to interact with LLM through the practice of prompt engineering
* Refine skills in prompt engineering to increase efficacy and quality of output
* Discover exploitable boundaries in LLM generation
* Develop a model of a story generation

These assignment learning outcomes contribute to the following course learning outcomes described in the [course syllabus](https://github.com/CMPSC350-Computational-Narrative-F2024/course_information):

1. Correctly describe and apply best practices of prompt engineering across a range of large language model (LLM) platforms to design successful prompts.
3. Demonstrate and criticize systemic bias, ethical issues, and failure modes inherent in language technologies such as LLMs.
4. Develop software to interact with language model application programmer interfaces (APIs).
5. Create and justify a body of text products that leverage text-to-text, text-to-image, and other language model technologies.

This assignment also contributes to the `Modes of Expression` and `Human Expression ` distribution learning outcome.

## Baseline Requirements

* Use a `programming language` of your choice to generate a `children's book` using `OpenAI API`. 
* Your book's content (text and images) must be generated using `OpenAI API`. 
* You must use an [assistant](https://platform.openai.com/docs/assistants/overview) with `Assistants API` as much as possible to create a cohesive flow for book generation. Essentially, you are building an application for yourself to generate a book. The generation process should be as automated and as streamlined as possible - you should not have to copy and paste things!
* The book's generated content must incorporate:
    - at least one constraint
    - environmental story-telling
    - your own grammar
    - images (at least 10)
* Your book must have a title and a front page cover.
* The generated book should range from ~500 to 1000 words, be oriented for ages 5-7, and follow your selected `theme`. If you are on the lower spectrum of generated text (closer to 500 words), you need more than 10 images. If your book is closer to 1000 words, 10 images is sufficient.
* Be creative. This book does not need to follow a standard story book format. For example, instead, it can be a poem, it have a representation of a card or another game. It can totally be weird. 
* The final version of the book should be in a PDF format that is printable. PDF should be automatically generated too!

### Assessment

In addition to participation in work-in-progress work described in the [Timeline section](#timeline), your final submission should include two (2) completed files for this assignment to be considered "complete". 

### `writing/report.md`

This contains documentation of all the prompts you have tried to use along with reflection on their uses. It should also include learning takeaways from this project.

### `src/main.py`

The program behind your story generation, including communication with the GPT API. If you use additional programs, include them in `src`.

Final submissions that do not include working code or a (mostly) completed report will be considered `Incomplete`. Individuals who do not participate in (most of) the `process` portions of the assignments will have their assignment marked as `Incomplete`.

### GatorGrade

You can check the baseline writing and commit requirements of this project by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python installed. If not, please see:

- [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
- [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
- [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, you need to install `gatorgrade`:

- First, [install `pipx`](https://pypa.github.io/pipx/installation/)
- Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Assistance

If you are having trouble completing any part of this project, then please talk with the course instructor or TLs during the laboratory sessions. Alternatively, you may ask questions in the Discord channel for this course. Finally, you can schedule a meeting during the course instructor's office hours.
