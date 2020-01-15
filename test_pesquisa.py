from splinter import Browser


def test_link_de_modulos():
    executable_path = {'executable_path':'./chromedriver'}
    with  Browser('chrome', **executable_path) as browser:    # Visit URL
        url = "http://www.google.com"
        browser.visit(url)
        
        browser.fill('q', 'Curso Python Pro')
        # Find and click the 'search' button
        button = browser.find_by_name('btnK')
        
        # Interact with elements
        button.click()
        browser.find_by_css('a[href="https://www.python.pro.br/"]').click()
        assert 'Módulos' == browser.find_by_css('a[href="/modulos/"]').first.text