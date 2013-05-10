import objc
import Foundation
import WebKit
import AppKit
#from PyObjCTools import AppHelper

class AppDelegate(AppKit.NSObject):
   def setApp_(self, app):
     self.app = app
   def windowWillClose_(self, notification):
     self.app.terminate_(self)

class MyApp(AppKit.NSApplication):

    win = None

    def makeWindow(self, dele):
        self.rect = Foundation.NSMakeRect(100,350,600,800)
        self.win = AppKit.NSWindow.alloc()
        self.win.initWithContentRect_styleMask_backing_defer_(self.rect, 
            AppKit.NSTitledWindowMask 
            | AppKit.NSClosableWindowMask 
            | AppKit.NSResizableWindowMask 
            | AppKit.NSMiniaturizableWindowMask, 
            AppKit.NSBackingStoreBuffered, 
            False)
        self.win.setTitle_("PsiTurk")
        self.win.setDelegate_(dele)
        self.win.display()
        self.win.orderFrontRegardless()      
        self.webview = WebKit.WebView.alloc()
        self.webview.initWithFrame_(self.rect)

        self.pageurl = Foundation.NSURL.URLWithString_("http://gureckislab.org")
        self.req = Foundation.NSURLRequest.requestWithURL_(self.pageurl)
        self.webview.mainFrame().loadRequest_(self.req)

        self.win.contentView().addSubview_(self.webview)
        self.win.setContentView_(self.webview)


    def bringToFront(self):
        self.activateIgnoringOtherApps_(True)
        self.win.makeKeyAndOrderFront_(True)


    def makeMenus(self):
        # Make statusbar item
        #self.setMainMenu_(None)
        #removeAllItems_()
        mainmenu = AppKit.NSMenu.alloc().init()
        app.setMainMenu_(mainmenu)

        fileMenu = AppKit.NSMenu.alloc().initWithTitle_("File")
        newMenu = AppKit.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit PsiTurk', "terminate:", 'q')
        fileMenu.addItem_(newMenu)

        fileMenuItem = AppKit.NSMenuItem.alloc().initWithTitle_action_keyEquivalent_("File", None, '')
        fileMenuItem.setSubmenu_(fileMenu)
        mainmenu.addItem_(fileMenuItem)
        fileMenuItem.setEnabled_(True)

    def setupApp(self):  # i did this because if you try doing in finshLoading() it'll load the .xib and overwrite the menu
        self.deleg = AppDelegate.alloc().init()
        self.deleg.setApp_(self)
        self.makeMenus()
        self.makeWindow(self.deleg)
        self.bringToFront()        

    def clicked_(self, notification):
        AppKit.NSLog('clicked!')


if __name__ == "__main__":
    app = MyApp.sharedApplication()
    app.setupApp()
    app.run()
    #AppHelper.runEventLoop()

