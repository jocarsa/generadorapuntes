window.onload = function() {
  var tocContainer = document.getElementById('table-of-contents');
  var contentContainer = document.getElementById('content');
  
  var headings = contentContainer.getElementsByTagName('h1');
  
  var tocList = document.createElement('ul');
  
  for (var i = 0; i < headings.length; i++) {
    var heading = headings[i];
    var pageNumber = getPageNumber(heading);
    
    heading.setAttribute('id', 'chapter' + (i + 1));
    
    var tocItem = document.createElement('li');
    var tocLink = document.createElement('a');
    tocLink.href = '#chapter' + (i + 1);
    tocLink.textContent = heading.textContent;
    
    tocItem.appendChild(tocLink);
    tocList.appendChild(tocItem);
    
    // Update the page number in the heading
    heading.textContent = heading.textContent + ' (Page ' + pageNumber + ')';
  }
  
  tocContainer.appendChild(tocList);
};

function getPageNumber(element) {
  var pageNumber = 0;
  
  while (element) {
    if (element.matches('body')) {
      break;
    }
    
    if (element.matches('h1')) {
      pageNumber++;
    }
    
    element = element.previousElementSibling;
  }
  
  return pageNumber;
}