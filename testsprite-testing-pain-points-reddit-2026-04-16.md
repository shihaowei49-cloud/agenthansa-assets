# Reddit research report: testing pain points from real user discussions

Checked on 2026-04-16.

Method:
- I sampled 17 distinct Reddit threads across r/node, r/devops, r/webdev, r/softwaretesting, r/QualityAssurance, r/Playwright, r/Everything_QA, r/learnprogramming, and r/IndieDev.
- I focused on posts that described concrete pain rather than generic opinions.
- I grouped the results into recurring themes, tool complaints, and universal frustrations that a new testing product could solve.

## Sampled threads

| # | Subreddit | Thread | URL | Primary signal |
|---|---|---|---|---|
| 1 | r/node | E2E Tests Taking Too Long. How you guys do it? | https://www.reddit.com/r/node/comments/1egrxks | E2E suites become too slow for normal CI use. |
| 2 | r/node | e2e tests in CI are the bottleneck now. 35 min pipeline is killing velocity | https://www.reddit.com/r/node/comments/1qzqmba/e2e_tests_in_ci_are_the_bottleneck_now_35_min/ | Slow end-to-end pipelines block PR feedback. |
| 3 | r/softwaretesting | Do you feel like your e2es just slow things down? And what do you do about it? | https://www.reddit.com/r/softwaretesting/comments/12raonb | Teams lose trust when UI suites are slow and brittle. |
| 4 | r/QualityAssurance | DOM-level E2E testing doesn't survive fast-moving products | https://www.reddit.com/r/QualityAssurance/comments/1qistft/domlevel_e2e_testing_doesnt_survive_fastmoving/ | DOM-driven tests fail to survive normal product change. |
| 5 | r/webdev | E2e testing for frontend developers, what's actually worth the time investment | https://www.reddit.com/r/webdev/comments/1r9ubwa/e2e_testing_for_frontend_developers_whats/ | Teams struggle to decide where E2E is worth the cost. |
| 6 | r/devops | How long do your pipelines take? | https://www.reddit.com/r/devops/comments/scqn87 | Long pipeline reruns create delivery friction. |
| 7 | r/devops | our ci/cd testing is so slow devs just ignore failures now | https://www.reddit.com/r/devops/comments/1qr00b5/our_cicd_testing_is_so_slow_devs_just_ignore/ | Slow test feedback trains teams to ignore failures. |
| 8 | r/QualityAssurance | E2E testing feels kinda broken. What are we all doing wrong? | https://www.reddit.com/r/QualityAssurance/comments/1ltnyym/e2e_testing_feels_kinda_broken_what_are_we_all/ | Users distrust "smart locators" and auto-healing claims. |
| 9 | r/QualityAssurance | manual testing bottleneck solutions: my team of 4 can't keep up with biweekly releases anymore | https://www.reddit.com/r/QualityAssurance/comments/1oewcqr/manual_testing_bottleneck_solutions_my_team_of_4/ | Manual regression turns QA into the release bottleneck. |
| 10 | r/Everything_QA | I'm so done with flaky Selenium tests... I feel like I'm babysitting my automation suite | https://www.reddit.com/r/Everything_QA/comments/1mnzx0c/im_so_done_with_flaky_selenium_tests_every_time_i/ | Selenium maintenance dominates QA time. |
| 11 | r/Playwright | 2 years into playwright and i'm still spending 70% of my time on test maintenance | https://www.reddit.com/r/Playwright/comments/1q1k3ah/2_years_into_playwright_and_im_still_spending_70/ | Switching tools does not remove the maintenance tax. |
| 12 | r/softwaretesting | Playwright alternative less maintenance burden, does this actually exist | https://www.reddit.com/r/softwaretesting/comments/1r6sqqw/playwright_alternative_less_maintenance_burden/ | Teams want lower-maintenance alternatives, not just new syntax. |
| 13 | r/QualityAssurance | Selenium tests breaking constantly after every UI change. Is test maintenance really supposed to take this much time? | https://www.reddit.com/r/QualityAssurance/comments/1oklz5j/selenium_tests_breaking_constantly_after_every_ui/ | UI shifts break Selenium suites and erode confidence. |
| 14 | r/QualityAssurance | Sorry-Cypress to Mochawesome due to budget issues, is it worthwhile? | https://www.reddit.com/r/QualityAssurance/comments/1it2f93/sorrycypress_to_mochawesome_due_to_budget_issues/ | Cypress ecosystem cost and migration pain are real buyer friction. |
| 15 | r/learnprogramming | Do people really write tests or it's just an elitism? | https://www.reddit.com/r/learnprogramming/comments/tpfh9t/do_people_really_write_tests_or_its_just_an/ | Developers still question whether writing tests is worth the effort. |
| 16 | r/IndieDev | I spent months writing unit tests for a game with no players, then I stopped | https://www.reddit.com/r/IndieDev/comments/1lcbdvq/i_spent_months_writing_unit_tests_for_a_game_with/ | Over-investing in tests too early feels wasteful. |
| 17 | r/softwaretesting | Browserstack - too expensive? Is our consultant SCAMMING us? | https://www.reddit.com/r/softwaretesting/comments/11gkv4s | Cross-browser infrastructure cost is a recurring complaint. |

## Top 5 pain themes

| Pain theme | Frequency in sample | Example threads |
|---|---:|---|
| Brittle UI automation and constant maintenance after product changes | 7 | #4, #8, #10, #11, #12, #13 |
| Slow E2E and CI feedback loops | 6 | #1, #2, #3, #6, #7 |
| Manual regression overload turns QA into a release bottleneck | 4 | #3, #7, #9, #10 |
| Tooling cost and migration friction | 4 | #12, #14, #17, #13 |
| Teams question the ROI of testing work when upkeep outweighs signal | 4 | #5, #11, #15, #16 |

## 3+ specific competitor and tool complaints

| Product or tool | What users complain about | Example threads |
|---|---|---|
| Selenium | Tests break on normal UI changes, selectors are fragile, async timing is painful, and maintenance becomes daily work. | #10, #13 |
| Playwright | Users see it as better than Selenium, but still report major maintenance burden once suites grow. | #11, #12 |
| Cypress / Sorry-Cypress | Teams complain about paid ecosystem costs and painful migration paths when tooling choices change. | #14 |
| BrowserStack | Buyers question whether the cross-browser convenience is worth the price unless legacy coverage is essential. | #17 |

## 3+ universal testing frustrations

1. Slow E2E suites destroy developer feedback loops and make CI feel like dead time.
   Evidence: #1, #2, #6, #7
2. UI automation often breaks on presentation-layer changes more often than on real product regressions.
   Evidence: #4, #8, #10, #11, #13
3. Manual regression work is repetitive, exhausting, and still difficult to replace safely.
   Evidence: #9, #10
4. Teams are tired of tools that promise "self-healing" or low-maintenance automation but still require constant babysitting.
   Evidence: #8, #11, #12

## Direct quotes from real Reddit users

> "We parallelized everything else. Builds take 2 min. Unit tests 3 min. Then e2e hits and its 35 minutes of waiting."

Source: https://www.reddit.com/r/node/comments/1qzqmba/e2e_tests_in_ci_are_the_bottleneck_now_35_min/

> "Every sprint it's the same nightmare. We knock out the new feature tests, then spend 3 days running through the same regression suite we've been doing for months."

Source: https://www.reddit.com/r/QualityAssurance/comments/1oewcqr/manual_testing_bottleneck_solutions_my_team_of_4/

> "I feel like I'm babysitting my automation suite instead of testing the product."

Source: https://www.reddit.com/r/Everything_QA/comments/1mnzx0c/im_so_done_with_flaky_selenium_tests_every_time_i/

> "every feature release means 15 to 20 tests need updates."

Source: https://www.reddit.com/r/Playwright/comments/1q1k3ah/2_years_into_playwright_and_im_still_spending_70/

> "i'm just a test maintenance engineer updating selectors all day."

Source: https://www.reddit.com/r/Playwright/comments/1q1k3ah/2_years_into_playwright_and_im_still_spending_70/

> "one tiny change in the UI and half the tests start crying."

Source: https://www.reddit.com/r/QualityAssurance/comments/1ltnyym/e2e_testing_feels_kinda_broken_what_are_we_all/

## Synthesis

The single biggest gap a new testing product could fill is this:

> Make UI and end-to-end testing resilient enough that teams get fast, trustworthy release signal without becoming full-time test-maintenance engineers.

What the sample suggests:
- Users do not just want "more automation." They want less upkeep.
- Teams are willing to automate critical paths, but they do not want DOM-level brittleness, 35-minute PR waits, or daily selector repair.
- Cost matters too. If a tool is expensive and still creates maintenance work, buyers start looking for alternatives quickly.

## What this means for a new testing product

The strongest wedge is not "we generate tests with AI."

It is:

1. Survive normal UI changes better than selector-heavy frameworks.
2. Keep CI feedback fast by prioritizing high-signal paths instead of brute-forcing every scenario.
3. Turn failures into actionable triage instead of more maintenance work.
4. Lower the skill burden for QA teams that cannot become full-time automation developers.

If a product can do those four things well, it is solving a pain pattern that showed up repeatedly across this Reddit sample.
