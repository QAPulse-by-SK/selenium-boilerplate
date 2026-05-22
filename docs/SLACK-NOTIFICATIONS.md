# Slack Notifications Guide
**QA Pulse by SK — Selenium Python Boilerplate**
🌐 www.skakarh.com

---

## GitHub Actions (built-in)

The CI workflow automatically sends Slack notifications on pass/fail.

**Setup:**
1. Create a Slack Incoming Webhook: https://api.slack.com/messaging/webhooks
2. Add `SLACK_WEBHOOK_URL` to GitHub repo secrets:
   - Repo → Settings → Secrets → Actions → New repository secret

That's it — the workflow handles the rest.

---

## Jenkins

Add to your Jenkinsfile `post` block:

```groovy
post {
    success {
        slackSend channel: '#qa', color: 'good',
            message: "✅ Selenium Tests Passed — ${env.JOB_NAME} #${env.BUILD_NUMBER}"
    }
    failure {
        slackSend channel: '#qa', color: 'danger',
            message: "❌ Selenium Tests Failed — ${env.JOB_NAME} #${env.BUILD_NUMBER} — ${env.BUILD_URL}"
    }
}
```

Requires the Jenkins Slack plugin.

---

## Azure DevOps

Add `SLACK_WEBHOOK_URL` as a pipeline variable (secret), then add a step:

```yaml
- script: |
    curl -X POST -H 'Content-type: application/json' \
    --data '{"text":"✅ Selenium Tests Passed"}' \
    $(SLACK_WEBHOOK_URL)
  displayName: Notify Slack
  condition: succeeded()
```
