Midterm
In this project, our team aims to create a simple divination software with a graphical user interface (GUI) to 
provide an easy-to-use interactive system. By the midterm stage, our goal is to complete the core code and implement the divination functionality.

Since the project topic was finalized, we have spent approximately 15 hours coding. In the source code, I created a dictionary to store the divination results. Since these results are based on Six Lines Divination (I Ching / Book of Changes), and the original text is written in Classical Chinese, I first translated the text into modern Mandarin and then used ChatGPT to extract the key information and translate it into English. There are a total of 8 × 8 = 64 possible divination outcomes, and we translated each one individually. This translation process took nearly 60% of our total time.

If we want the code to run more efficiently, we could try using binary encoding instead of characters to improve dictionary lookup speed (e.g., ['1' if line == yang else '0' for line in lines]). However, we are not sure if this optimization is necessary.

In the source code, we did not use any initial code or third-party libraries. However, we added some additional features to the previous code to ensure that the user input consists of three-digit numbers rather than other numbers or blank characters. Additionally, we optimized the logic of the divination result output to ensure more accurate and precise results.
