#!/usr/bin/env python
"""from simple_app import app

if __name__ == '__main__':
    port = 5000
    print(f"Starting server at http://localhost:{port}")
    app.run(host='localhost', port=port, debug=True) """

import os
from simple_app import app  # make sure this points to your actual app instance

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's provided PORT
    app.run(host="0.0.0.0", port=port, debug=True)

