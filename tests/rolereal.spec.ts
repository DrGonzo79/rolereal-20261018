import {test,expect} from "@playwright/test";
test.beforeEach(async({page})=>{await page.goto("./");await expect(page.locator("body")).toHaveAttribute("data-hydrated","true");});
test("student completes the honest shift and sees a debrief",async({page})=>{
 await expect(page.getByRole("heading",{name:/Try the shift/})).toBeVisible();
 for(const answer of ["Assess the newly confused patient","Hold it and escalate through charge nurse/pharmacy","Give report, then finish concise factual notes"]){await page.getByRole("button",{name:answer}).click();await page.getByRole("button",{name:/Continue|See my debrief/}).click();}
 await expect(page.getByRole("heading",{name:"Your honest debrief"})).toBeVisible();
 await expect(page.getByText("Strong fit for the trade-offs")).toBeVisible();
 await page.getByRole("button",{name:"Try again"}).click();
 await expect(page.getByText("The handoff is already behind")).toBeVisible();
});
test("career switch and mobile layout work",async({page})=>{
 await page.setViewportSize({width:375,height:812});await page.reload();
 await page.getByRole("button",{name:/Electrician apprentice/}).click();
 await expect(page.getByText("Scenario in practitioner review")).toBeVisible();
 expect(await page.evaluate(()=>document.documentElement.scrollWidth>document.documentElement.clientWidth)).toBeFalsy();
});
