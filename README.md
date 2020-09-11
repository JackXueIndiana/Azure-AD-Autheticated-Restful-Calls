# Azure-AD-Authenticated-Restful-Calls

Microsoft Azure Active Directory Authentication Library is in version 1.2.4 now. Its refresh tokening mechanism is sued by a number new Azure services. Here we provide an example on how to use this library to access Azure Graph.

You need to first install the package: pip install adal

You also need to do a Application Registration in Azure Portal, from which you will get the client ID and client secret.

Once you have the client ID you can ask Azure Graph team to associate this client ID with your account.

With all these now you can update the code we provide to run the code that will does two things:
1. Get AAD token for you, which will expired in a short time period.
2. With this token you call the Azure Graph RESTful API and get the info you need.

