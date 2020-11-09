'use strict'

module.exports = {
  'sample test': function(browser) {
    browser
      .url(browser.launch_url)
      .waitForElementVisible('#id_username', 1000)
      .expect.element('#id_username')
      .text.to.equal('')
    browser.end()
  }
}
