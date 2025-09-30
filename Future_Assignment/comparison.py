from collections import Counter




# ==================
# MODELS
# ==================
CHATGPT = "openai/gpt-4o"   # ChatGPT model
NOTEBOOKLM = "notebooklm"   # Placeholder – update if SDK/endpoint differs

EVALS = ["is_good_summary", "summary_quality_assessment", "factual_accuracy"]

DATASET = [
    {
        "id": 1,
        "document": """Introduction
                    “75% of AI projects fail to reach production” has become a rallying cry in boardrooms and technical forums alike. In practice, teams observe sudden latency spikes when an LLM struggles under real-world load and silent regressions that only surface when users flag wrong or harmful outputs. Behind these symptoms lie brittle evaluation methods that pass only narrow test cases, a lack of end-to-end AI observability, and manual QA bottlenecks that slow down feedback loops. What would it take to close this reliability gap?

                    Snapshot benchmarks like GLUE and SuperGLUE are good for quickly checking a model's language skills in controlled tests, but they don't pick up problems that happen when a system is live. Because these static tests use fixed datasets and don't often overlap with different user inputs, they can't see data drift or adversarial probes. They also only look at small language-understanding problems instead of whole user interactions. A misleading impression of preparation is often conveyed when models achieve ceiling performance on these tasks.

                    Alternatively, real-time evaluation keeps a close watch on essential metrics once your AI is live:

                    Latency and throughput: How quickly and reliably the model responds when demand spikes.

                    Concept and data drift: When new inputs stray from the patterns the model was trained on.

                    Toxicity and safety scores: Keeping outputs within safe, acceptable limits.

                    By keeping an eye on these signals and comparing them to how happy users are, teams can find small problems before they get worse. This changes the way we deal with problems from putting out fires after they happen to keeping things in good shape before they happen. To be sure that LLMs will work, you have to keep testing them.

                    In this article, you'll learn how to build real-time evaluation pipelines, pick the right metrics, and use observability tools to make sure your models stay strong in production.


                    Understanding Real-Time LLM Evaluation
                    2.1 Traditional vs. Real-Time Evaluation Comparison
                    Traditional benchmarks such as GLUE and SuperGLUE run on fixed datasets and give a one-off snapshot of language understanding, but they stay blind to live issues like data drift and unexpected user prompts. Once a model passes these tests, teams often assume it’s ready for production, only to face surprises under real-world load . Real-time evaluation, by contrast, tracks metrics continuously latency, error rates, toxicity scores, and user feedback so you see how your model behaves as conditions change.

                    Traditional tests catch broad performance gaps but miss microbursts of failure that frustrate users think a 10-second slowdown or a sudden spike in harmful outputs. Real-time systems flag those events immediately and tie them back to specific inputs, letting engineers roll out fixes before issues scale. That shifts teams from reacting to incidents after users complain to preventing incidents before they impact anyone.

                    2.2 Production Challenges
                    When you move an LLM into production, you face new hurdles that static tests simply don’t cover:

                    Scale: Hundreds or thousands of concurrent requests can expose performance bottlenecks invisible in small-scale tests.

                    Variability: Real user inputs vary widely emoji, slang, typos and models can fail unpredictably when they hit unfamiliar patterns.

                    Expectations: Users expect near-instant answers with high reliability; even short delays or off-tone responses erode trust.

                    These factors make continuous monitoring not just nice to have, but essential.

                    Waiting hours or days to notice a model’s silent regression harms both users and the bottom line. Retailers, for example, lose $1.1 trillion globally each year from slow data responses outdated inventory forecasts, missed sales, excess stock. When your LLM starts hallucinating or slows down, every minute of blind operation costs money and reputation.


                    Core Components of Real-Time Evaluation Systems
                    3.1 Metrics Collection Layer
                    This layer collects the basic numbers you need to see how well the model is working with live traffic.

                    Metrics for performance (latency, throughput): Learn how long each request takes and how many you can handle in a second. By watching API latency and throughput in real time, you can find slowdowns or capacity problems before they affect users.

                    Quality measures (usefulness and correctness): When you can, compare the outputs to the real thing, or use LLM-as-judge methods like G-Eval for tasks that don't have a set structure. When the inputs change, checking for relevance and correctness keeps your model on track.

                    Safety measures (finding bias and harmfulness): You can find harmful or biased content in real time by using classifiers or finely tuned toxicity scorers. If you always keep an eye on bias categories like race and gender, outputs won't go in the wrong direction.

                    3.2 Processing Pipeline
                    You can only use raw metrics if you make them into signals that you can act on. This pipeline does that.

                    Architecture for processing streams: Use tools like Apache Flink or Kafka Streams to constantly collect and analyze metrics. These tools let you change and mix data on the fly, which is what your traffic needs.

                    Algorithms for scoring in real time: When new data comes in, you can use sliding windows or incremental scoring to find moving averages, percentile latencies, or anomaly scores. This lets you find outliers, like an error rate that suddenly goes up, in seconds instead of hours.

                    How to send warnings: You can set up your pipeline to send alerts to services like PagerDuty, Slack, and email when important thresholds are crossed. For example, when p95 latency goes over 500 ms. Make your alert rules less noisy and more focused on real problems in production.

                    3.3 Feedback Integration
                    Evaluation isn't done until the insights go back to make the model or system better.

                    Feedback loops from users: Get clear ratings, thumbs-up/down, or error reports with comments from end users. Put these signals into your monitoring dashboard to see how technical metrics match up with how happy real users are.

                    Automatic correction systems: Use AI agents or scripts that follow rules to automatically fix simple problems, such as changing harmful comments before they get to users. This "first-pass" filter lets you make more permanent changes without stopping service.

                    Getting information from data about production: Periodically retrain or fine-tune models on a carefully chosen set of real-world questions and errors that have been marked. This keeps your LLM up to date on how people use language, new topics, and new edge cases.


                    Step-by-Step Implementation Guide
                    Step 1: Infrastructure Setup
                    Getting your foundation right means choosing the right monitoring platform, plumbing in telemetry, and ensuring you can store metrics at scale.

                    Choosing monitoring tools (Future AGI): Future AGI offers end-to-end evaluation and tracing to catch silent regressions and optimize LLMs post-deployment.

                    Putting together data pipeline: When using Future AGI, detailed data pipeline setup is not required, as it can be done very easily via OpenTelemetry (OTEL). This handles sending logs of LLM requests and responses to your monitoring stack seamlessly. Set up your application or agent framework (LangChain, LlamaIndex, or custom middleware) to send structured events with timestamps, model IDs, prompts, responses, and metadata for each call. Make sure you tag events with user or session IDs so you can group metrics by cohort.

                    Putting together storage systems: Similarly, when using Future AGI with OTEL, custom storage systems are not required. It manages logs, metrics, and traces efficiently, allowing you to focus on analysis rather than infrastructure. For long-term trends, keep detailed data for 30 to 90 days and aggregate older data into summaries as needed.

                    Step 2: Metric Definition and Baseline Establishment
                    With your pipes and store in place, decide what to measure and what “good” looks like before you go live.

                    Selecting relevant KPIs: Define performance metrics like p50/p95 latency and throughput in requests per second to catch slowdowns early. For quality metrics like accuracy or relevance scores, note that LLM-as-judge methods have limitations such as potential inconsistencies in judgments, while human-verified approaches can be resource-intensive. Future AGI provide high-quality evaluations with custom evals, offering a scalable and reliable way to assess core tasks. Include safety metrics like bias classifications or toxicity scores using off-the-shelf detectors or custom classifiers.

                    Setting up performance standards: Run load tests in pre-production to get baseline latency and error rates for expected traffic patterns. If you can, use historical production data to set reasonable limits for drift and correctness. These baselines on a common dashboard show everyone what "normal" looks like.

                    How to set the limits for alerts: If the p95 latency is higher than 500 ms or the error rate is higher than 1%, you can set up PagerDuty, Slack, or email alerts to go off right away. Use different alerts for quality problems (when accuracy drops) and capacity problems (when throughput drops) to send the right teams to the right place. To keep people from getting too many alerts, add levels like "warning" and "critical."

                    Step 3: Testing Framework Development
                    Don't rely on manual QA to find regressions; make sure that every step is checked automatically.

                    Automated test suite creation: Every time you change the model, look at the list of common prompts and expected outcomes. Put these tests in your CI pipeline so that the build will fail if any changes make it less safe or of lower quality. To account for every conceivable production scenario, be sure to include edge cases such as typos, slang, and intentionally difficult inputs.

                    A complete set of tools for doing A/B testing: To immediately observe the impact on the key performance indicators, use a canary model or implement a change with real traffic. Before you send it to a lot of people, use statistical methods like sequential testing to find big differences in latency, accuracy, or toxicity. Get thumbs up or down from users to connect numbers with real feedback.

                    Rules for regression testing: After each deployment, run a regression suite on fake data and live shadow traffic to make sure that no failures that weren't obvious got through. To make it easier to check, keep regression results in a dataset with versions. If any important tests fail or quality drops below the alert level, promotions should be stopped right away.

                    Step 4: Dashboard and Alerting Setup
                    Make your metrics visible and actionable for AI/ML engineers and decision-makers, with a focus on LLM-specific insights.

                    Real-time visualization: Use Future AGI for built-in dashboards that display live charts of AI/ML metrics like latency percentiles, error rates, drift scores, toxicity levels, and user ratings. Embed drill-downs to trace issues back to specific prompts, responses, or model behaviors

                    Views that are specific to stakeholders: Create specific panels within Future AGI like ML engineers can monitor quality and drift dashboards, while product owners get high-level overviews of model uptime, accuracy, and satisfaction. Limit access to sensitive data (like raw prompts or user inputs) based on roles to ensure compliance in AI/ML pipelines.

                    How to escalate things: Set up automated alerts in Future AGI for AI/ML thresholds, such as spikes in toxicity or drift, routing notifications directly to on-call ML teams for quick resolution and model adjustments.

                    Real-Time LLM Evaluation implementation pyramid showing continuous testing phases: infrastructure, metrics, framework, dashboards
                    Figure 1: LLM Monitoring Implementation


                    Common Pitfalls and How to Avoid Them
                    Too much monitoring can make people tired of alerts.

                    Sending too many alerts, especially ones that don't matter or are false positives, makes teams numb to real problems. When there are more alerts than problems that need to be fixed, responders start to ignore them, which slows down their responses to important events. Set your alert thresholds so that you only get alerts for big changes, and group related alerts into digest summaries to stop this from happening.

                    There isn't enough baseline data.

                    Teams can see problems coming when everything is going well, but they can't tell the difference when things aren't going well. You won't be able to set reasonable alert levels if you don't do a load test before you deploy or look at metrics from the past. During the pre-production and early production phases, you should always keep an eye on baseline KPIs like latency, error rates, and quality scores. This will help you keep an eye on things in the future.

                    Ignoring edge cases in production

                    Edge cases, which are rare inputs or usage patterns, often show bugs that regular tests miss. Your model could break if you only test it with common situations and then run into typos, slang, or data formats that you didn't expect. Make a small library of real-world examples from logs and add them to your test suite to find bugs before they affect users.

                    Bad rules for communication between teams

                    When data science, engineering, and operations teams don't talk to each other, important context can get lost. When people don't know where to hand things off or don't have access to shared documentation, incident response slows down and problems keep piling up. Set up regular syncs, a shared incident runbook, and role-based alert routing so that everyone knows when and how to get involved.


                    Advanced Techniques and Future Considerations
                    Continuous evaluation is moving away from set limits to smart systems that can find problems without rules and predict failures. Teams are using AI-driven insights to keep models sharp, safe, and in line with user needs by adding assessment to development pipelines.

                    Finding strange things with AI: Modern methods use machine learning and LLMs to learn how requests usually go and automatically flag any changes. By only looking at statistically unusual outputs, this method cuts down on the number of noisy alerts. It can also change as needed without having to write new rules by hand.

                    Models for predicting evaluation: Teams train models to predict drops in quality or spikes in latency based on signals from upstream sources like data drift or token distributions, so they don't have to wait for things to go wrong. These systems can start retraining or giving out more resources before any problems come up. This makes sure that SLAs are not affected.

                    Adding to CI/CD pipelines: Adding LLM assessment to CI/CD makes sure that every code or prompt update goes through automated tests and live shadow traffic checks. This setup catches regressions early, enforces quality gates, and keeps deployments safe by comparing canary and baseline models on real metrics.

                    Emerging trends in real-time evaluation: Look for self-monitoring LLMs that attach confidence scores to responses and adjust behavior on the fly. Federated evaluation across edge and cloud, multimodal monitoring for audio/image/text, and explainability metrics are all on the horizon as teams demand deeper, broader insight.


                    Conclusion
                    Real-time LLM evaluation makes one-time checks into a safety net that works all the time. It watches latency, accuracy, and toxicity so you can fix problems before they hurt users. It gets rid of slow, manual QA cycles and replaces them with dashboards and alerts that run on their own. This can lower the average time it takes to fix things and the amount of time they are down by up to 60%. You can build an evaluation system that adapts to new data and data drift by combining a metrics collection layer, a stream processing pipeline, and feedback loops. Advanced teams use AI-powered anomaly detection and predictive models to find out when quality will drop or latency will rise before they reach SLAs. Adding testing to CI/CD pipelines makes sure that quality gates are in place, runs canary tests, and stops releases that aren't safe.

                    In the first two weeks, do a pilot to make sure everything goes well. Pick the tools you want to use to keep an eye on things, set up data pipelines, and get your baseline KPIs. In weeks 3–6, add to your automated test suites, regression checks, and dashboards that show data in real time. Use feedback from the beginning to change the alert thresholds. By the third month, go into full production: add predictive evaluation, anomaly scoring, and user feedback loops for full coverage from start to finish.""",
        "chatgpt_summary": """well-cited industry concern is that 75% of AI projects fail to reach production, largely due to fragile evaluation methods, lack of observability, and manual QA bottlenecks. Traditional benchmarks like GLUE and SuperGLUE provide a one-time snapshot of language ability but fail to capture real-world issues such as latency spikes, data drift, or harmful outputs. This gap calls for real-time evaluation—continuous monitoring of performance, safety, and user experience once models are live.
                    Why Traditional Tests Fall Short
                    Static benchmarks evaluate narrow tasks in fixed conditions, leading to a false sense of readiness. Once deployed, models encounter scale, diverse inputs, and user expectations that static tests cannot anticipate. Latency, variability in prompts (slang, emojis, typos), and trust-sensitive responses pose unique challenges. Failures here lead to reputational and financial damage—retailers, for example, lose over $1 trillion annually from slow or inaccurate systems.
                    Core Components of Real-Time Evaluation
                    1.
                    Metrics Collection Layer
                    o
                    Performance: Latency and throughput monitoring to detect bottlenecks.
                    o
                    Quality: Comparing outputs to ground truth or using LLM-as-judge methods.
                    o
                    Safety: Real-time detection of bias, toxicity, and harmful responses.
                    2.
                    Processing Pipeline
                    o
                    Stream processing tools (e.g., Kafka, Flink) convert raw data into actionable signals.
                    o
                    Techniques like sliding windows and anomaly scoring flag unusual spikes in latency or error rates.
                    o
                    Alerts are routed through channels like Slack or PagerDuty, with noise-reduction strategies to avoid alert fatigue.
                    3.
                    Feedback Integration
                    o
                    User feedback loops (ratings, reports) enrich dashboards with real satisfaction data.
                    o
                    Automated correction systems filter harmful outputs before delivery.
                    o
                    Retraining on real-world data ensures models evolve with usage trends and edge cases.
                    Implementation Guide
                    •
                    Step 1: Infrastructure Setup Choose monitoring platforms (e.g., Future AGI with OpenTelemetry) to track structured events, store metrics, and manage logs.
                    •
                    Step 2: Metric Definition & Baselines Define KPIs like latency percentiles, accuracy, and toxicity scores. Use load tests to establish thresholds and create clear alert rules.
                    •
                    Step 3: Testing Framework Development Automate test suites within CI pipelines, including edge cases like slang and typos. Use A/B testing and regression checks to validate deployments before scaling.
                    •
                    Step 4: Dashboards & Alerting Build role-specific dashboards (engineers vs. product owners). Enable real-time drill-down into issues and set escalation paths for critical failures.
                    Common Pitfalls
                    •
                    Alert Fatigue: Too many false positives dilute urgency; thresholds must balance sensitivity and noise.
                    •
                    Weak Baselines: Without historical metrics, teams cannot differentiate between normal and abnormal states.
                    •
                    Ignored Edge Cases: Overlooking rare but realistic inputs (e.g., typos, slang) leads to unexpected failures in production.
                    •
                    Poor Team Coordination: Siloed operations between engineering and data science hinder incident response.
                    Advanced Techniques & Future Trends
                    •
                    AI-Driven Anomaly Detection: Machine learning models detect statistically unusual outputs, reducing reliance on static rules.
                    •
                    Predictive Evaluation Models: Forecast performance drops or spikes in latency, allowing proactive fixes.
                    •
                    Integration with CI/CD: Continuous evaluation ensures every code or model update passes automated quality gates before release.
                    •
                    Emerging Practices: Self-monitoring LLMs with confidence scoring, multimodal monitoring, and federated evaluation across cloud and edge are on the horizon.
                    Conclusion
                    Real-time evaluation transforms AI monitoring from reactive troubleshooting to proactive assurance. By continuously tracking latency, quality, and safety, organizations can reduce downtime and incident response time by up to 60%. A phased rollout—starting with pilot monitoring, followed by test suite expansion, and culminating in predictive evaluation—ensures reliable and adaptive systems in production.
                    Ultimately, continuous, intelligent monitoring bridges the gap between static benchmarks and dynamic real-world use, enabling LLMs to deliver consistent, safe, and trustworthy performance at scale.""",
         "notebooklm_summary": """A significant number of AI projects, reportedly 75%, fail to make it to production. Even when they do, teams often face issues like sudden latency spikes under real-world loads and silent performance regressions that only come to light after users report incorrect or harmful outputs. These problems often stem from reliance on traditional, brittle evaluation methods, a lack of comprehensive AI observability, and slow manual quality assurance processes. To bridge this reliability gap, a shift from static, pre-deployment benchmarks to continuous, real-time evaluation is essential.
                                The Shortcomings of Traditional Evaluation
                                Traditional benchmarks like GLUE and SuperGLUE offer a snapshot of a model's language understanding skills in a controlled environment. However, they are ill-equipped to identify problems that emerge once a system is live. These static tests use fixed datasets that may not align with the variety of real user inputs, leaving them blind to issues like data drift and adversarial attacks. They focus on narrow language tasks rather than complete user interactions, often creating a misleading sense of production readiness. While these tests can catch broad performance gaps, they frequently miss smaller failures, such as a brief slowdown or a sudden increase in harmful outputs, which can frustrate users and erode trust. When an LLM begins to hallucinate or slow down, every minute it operates without being noticed can cost a business money and damage its reputation.
                                Embracing Real-Time Evaluation
                                In contrast, real-time evaluation continuously monitors key metrics while an AI model is in production, allowing teams to see how it behaves as conditions change. This approach shifts teams from a reactive stance, where they fix problems after users complain, to a proactive one, where they prevent issues from impacting anyone in the first place.
                                A robust real-time evaluation system consists of several core components
                                •
                                Metrics Collection: This layer gathers raw data on the model's performance, quality, and safety. It tracks performance metrics like latency and throughput, quality indicators such as correctness and relevance (often using LLM-as-judge methods), and safety scores to detect bias and toxicity.
                                •
                                Processing Pipeline: Raw metrics are transformed into actionable signals using stream processing tools like Apache Flink or Kafka Streams. This pipeline employs real-time scoring algorithms to calculate moving averages or identify anomalies, allowing teams to spot outliers in seconds rather than hours. When key thresholds are crossed—for example, if latency exceeds 500 ms—the system sends automated alerts to services like PagerDuty or Slack.
                                •
                                Feedback Integration: The insights gained from monitoring are fed back into the system to improve the model. This includes integrating direct user feedback (e.g., ratings or error reports) and building automated correction systems to filter out simple issues like harmful content. Critically, production data is used to periodically retrain or fine-tune models, keeping them updated on new language patterns, topics, and edge cases.
                                Implementing a Real-Time System
                                Building such a system involves a step-by-step process. First, the right infrastructure, including monitoring tools like Future AGI and data pipelines, must be set up. Second, teams must define key performance indicators (KPIs) for performance, quality, and safety, and establish baseline performance standards through pre-production load testing. Third, an automated testing framework should be developed to catch regressions before they reach users, incorporating A/B testing and comprehensive regression suites. Finally, real-time dashboards and alerts should be configured to make metrics visible and actionable for different stakeholders, from engineers to product owners.
                                Future Directions
                                The field of continuous evaluation is evolving toward more intelligent systems. Advanced techniques include AI-driven anomaly detection that learns normal behavior and flags deviations without needing predefined rules. Predictive models are also being developed to forecast drops in quality or spikes in latency based on upstream signals like data drift, enabling preemptive action. Furthermore, by integrating evaluation directly into CI/CD pipelines, teams can enforce quality gates and ensure every deployment is safe and reliable. Emerging trends point towards self-monitoring LLMs that can adjust their own behavior and provide confidence scores for their responses.
                                By adopting real-time evaluation, organizations can create an adaptive safety net that continuously monitors LLM performance, significantly reducing downtime and the time it takes to resolve issues. This proactive approach replaces slow, manual QA cycles with automated dashboards and alerts, ensuring models remain robust, safe, and effective in the dynamic environment of production."""
    }
    
]

# ======================
# HELPER FUNCTIONS
# ======================
def word_overlap(doc, summary):
    doc_words = set(doc.lower().split())
    summary_words = summary.lower().split()
    overlap = sum(1 for w in summary_words if w in doc_words)
    return round(overlap / max(len(summary_words), 1), 3)

def length_ratio(doc, summary):
    return round(len(summary.split()) / max(len(doc.split()), 1), 3)

def compare_summaries(doc, chat_summary, note_summary):
    overlap_chat = word_overlap(doc, chat_summary)
    overlap_note = word_overlap(doc, note_summary)
    len_chat = length_ratio(doc, chat_summary)
    len_note = length_ratio(doc, note_summary)
    
    # Decide better summary
    better = "ChatGPT" if overlap_chat >= overlap_note else "NotebookLM"
    
    # Generate simple highlights
    highlights = []
    if overlap_chat > overlap_note:
        highlights.append("ChatGPT covers more content from the document.")
    elif overlap_note > overlap_chat:
        highlights.append("NotebookLM covers more content from the document.")
    else:
        highlights.append("Both summaries have similar content coverage.")
    
    if len_chat > len_note:
        highlights.append("ChatGPT summary is longer, possibly more complete.")
    elif len_note > len_chat:
        highlights.append("NotebookLM summary is longer.")
    
    return {
        "overlap_chat": overlap_chat,
        "overlap_note": overlap_note,
        "len_chat": len_chat,
        "len_note": len_note,
        "better_summary": better,
        "highlights": highlights
    }

# ======================
# RUN COMPARISON
# ======================
results = []
for item in DATASET:
    comp = compare_summaries(
        item["document"],
        item["chatgpt_summary"],
        item["notebooklm_summary"]
    )
    comp["id"] = item["id"]
    results.append(comp)

# ======================
# DISPLAY RESULTS
# ======================
print(f"{'ID':<4}{'ChatGPT Overlap':<18}{'NotebookLM Overlap':<20}{'ChatGPT Len':<14}{'NotebookLM Len':<16}{'Better Summary':<15}")
for r in results:
    print(f"{r['id']:<4}{r['overlap_chat']:<18}{r['overlap_note']:<20}{r['len_chat']:<14}{r['len_note']:<16}{r['better_summary']:<15}")

# ======================
# DISPLAY HIGHLIGHTS
# ======================
print("\n=== Detailed Highlights per Document ===")
for r in results:
    print(f"\nDocument ID: {r['id']}")
    for h in r['highlights']:
        print(f"- {h}")
