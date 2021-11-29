This script helps create a long wordlist from the Wikimedia dump where articles of the Odia-language Wikipedia, word entries of the Odia Wiktionary and texts of the Odia Wikisource are uploaded on a regular basis for community use and research. A wordlist is generally used for a range of research Natural Language Processing (NLP). Some common use cases of a wordlist includes creating a spell-check engine (or predictive text for helping with input on mobile devices), dictionary or even recording pronunciation of words in a language. The [original script](https://github.com/tshrinivasan/tamil-wikipedia-word-list) was written by our friend T. Shrinivasan which he then guided OFDN's Subhashish Panigrahi during a session for accomodating the needs of Odia. 

# Step 1: Download data dump

Download the Wikimedia dumps. You can find all latest dumps from [this link](https://dumps.wikimedia.org/backup-index.html) (look up for "orwiki" for Odia Wikipedia, "orwiktionary" for Odia Wiktionary and "orwikisource" for Odia Wikisource).

Alternatively, you can also download specific files for each project (for inatance, you want to download only the titles of Odia Wikipedia and not the content of all the articles or just the category names). Check [here](https://dumps.wikimedia.org/orwiki/) for Odia Wikipedia, [here](https://dumps.wikimedia.org/orwikisource/) for Odia Wikisource, [here](https://dumps.wikimedia.org/orwiktionary/) for Odia Wiktionary. The folder name "latest" will show you the latest dump and above that folder link you can find some recent historical dumps.

# Step 2: Extract XML file

We are using the example of Odia Wikipedia below on a Unix computer (Linux and MacOS included) but the same process applies for a file from any other Wikimedia project. In case you are visiting the folder link as explained above, you could see the explainatory file names such as "orwiki-latest-pages-articles-multistream.xml.bz2". Download the file from the directory and extract/unzip. You can use the below command line by opening your computer terminal (On MacOS press Cmd+Space bar >> type "terminal" >> Enter).

```
bunzip2  orwiki-latest-pages-articles-multistream.xml.bz2
```

# Remove all English (Latin) characters that are not required
To create a wordlist you will need to have Python installed (mostly pre-installed in most modern Unix computers). You need to download and extract this Github repository either by using command line or as a [ZIP file](https://github.com/ofdn/odia-wordlist-from-wikimedia-dump/archive/refs/heads/master.zip). Once unzipped copy the file called "create_wordlist.py" to the folder where you have the Wikimedia data dump. 

Run on terminal

```
python create_wordlist.py 
```

## BONUS: Count the total number of unique words

```
wc -l unique_odia_words.txt
1200 unique_odia_words.txt
```

##### sort the words

If you want to sort the words, run the below command.

```
sort unique_odia_words.txt > unique_odia_sorted_words.txt
```

This will sort the words in the file "unique_odia_sorted_words.txt".
