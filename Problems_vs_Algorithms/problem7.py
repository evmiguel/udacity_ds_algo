# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.handler = None
        self.path = None
        self.children = {}

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            child = RouteTrieNode()
            child.path = path
            self.children[path] = child

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        for path in paths:
            node.insert(path)
            node = node.children.get(path)
        node.handler = handler

    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.root
        for path in paths:
            if path not in node.children:
                return None
            node = node.children.get(path)
        return node.handler

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        self.route_trie = RouteTrie()
        self.root_handler = root_handler
        self.not_found_handler = not_found_handler
        # You could also add a handler for 404 page not found responses as well!

    def remove_trailing_slash(self, path):
        return path[:-1]


    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        assert isinstance(path, str) and isinstance(handler, str)
        paths = self.split_path(path)
        self.route_trie.insert(paths, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        assert path

        if path == '/' and len(path) == 1:
            return self.root_handler

        paths = self.split_path(path)
        handler = self.route_trie.find(paths)

        return handler if handler else self.not_found_handler


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        # Check trailing slash
        if path[len(path)-1] == '/':
            path = self.remove_trailing_slash(path)
        return path.split('/')


# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # 'root handler'
print(router.lookup("/home")) # 'not found handler'
print(router.lookup("/home/about")) # 'about handler'
print(router.lookup("/home/about/")) # 'about handler'
print(router.lookup("/home/about/me")) # 'not found handler'

# Test empty string
try:
    router.lookup("")
except AssertionError:
    pass

# Test None values
try:
    router.add_handler(None, None)
except AssertionError:
    pass
