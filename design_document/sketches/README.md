# Django: Wiki
### Sigrid van Klaveren - 14080702
### Minor Programmeren

An implementation of a website similar to Wikipedia. This website has several pages with information. The user is able to navigate through different pages, search for pages and add new pages. 


## Required HTML files

- layout.html already exists. This file describes the broader structure for a page
- index.html also exists. This is a template for the index view.
- html file for specific entry page
- html file for the search results
- html file for creating a new page
- html file for editing a page that already exists
- html file for error page. This shows if an entry does nog exist 

## Screen designs

### Index
![Index page](/design_document/sketches/Index@1x.png)

### Search results

![Search results page](/design_document/sketches/Search_results@1x.png)

### Entry page

![Entry page](/design_document/sketches/Entry@1x.png)

### New page

![New page](/design_document/sketches/New_page@1x.png)

### Error page

![Error page](/design_document/sketches/Error@1x.png)

### Edit page

![Edit page](/design_document/sketches/Edit@1x.png)


## Navigation between screens
### Menu on the right
This is for all pages the same. 
- Home: go to index page
- Create New Page: go to 'new page' page
- Random: has no functionality yet
- Search bar: when enter-key is pressed go to entry page if it exists. Otherwise go to search results page

### Search results page
- Title {1}: go to that entry page
- Textbox: go to that entry page

### Entry, Edit and New page
- Edit page: go to Edit page
- Save page: go to entry page, give errormessage if title already exists.
- Textbox: if the border is visible, you can edit the text
