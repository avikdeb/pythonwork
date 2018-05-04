from jira.client import JIRA

jira_server = "https://avikpersonal.atlassian.net"
jira_user = "avikdeb@hotmail.com"
jira_password = "Ayutasouri74"

jira_server = {'server':jira_server}
jira = JIRA(options=jira_server, basic_auth=(jira_user, jira_password))

group = jira.group_members("site-admins")
for users in group:
    print(users)

issue = jira.issue("PYT-1")
print("JIRA Project Key --> " + issue.fields.project.key)
print("JIRA Issue Type --> " + issue.fields.issuetype.name)
print("Issue Reported By --> " + issue.fields.reporter.displayName)
print("Issue Assigned To --> " + issue.fields.assignee.displayName)
