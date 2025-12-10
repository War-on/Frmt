document.evaluate('//*[@id=\&quot;region-main\&quot;]/div/div/div/h2', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.textContent='';
document.querySelector('.no-link').remove();
