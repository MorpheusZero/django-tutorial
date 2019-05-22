from django.http import HttpResponse


def index(request):
    return HttpResponse("""
      <html>
         <head>
            <title>
               Dylan Test
            </title>
         </head>
         <style>
            html, body {
               margin: 0;
               width: 100%;
               height: 100%;
               padding: 0;
            }

            .content {
               width: 80%;
               margin: 20px auto;
               border: 1px solid gray;
               box-shadow: 1px 2px 3px lightgray;
               padding: 12px;
               text-align: center;
            }

            .content > h3 {
               margin: 4px;
            }
         </style>
         <body>
            <div class="content">
               <h3>My Test App</h3>
            </div>
         </body>
      </html>
    """)
