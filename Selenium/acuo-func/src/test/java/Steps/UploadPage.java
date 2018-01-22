package Steps;

import Base.BaseUtil;
import cucumber.api.java.en.And;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.testng.Assert;

public class UploadPage extends BaseUtil {
    private BaseUtil base;

    public UploadPage(BaseUtil base) {
        this.base = base;
    }

    @Given("^Navigate to upload page$")
    public void navigateToUploadPage() throws Throwable {
        WebElement element;
        element = base.Driver.findElement(By.xpath("//div[@class='UploadPortfolio__text___3USYJ']"));
        element.click();
        //Check if browser navigate to correct page/URL.
        //If the URL is incorrect, fail the test.
        String expectedUrl = "https://uat.acuo.com/#/upload_portfolio";
        try{
            Assert.assertEquals(expectedUrl,base.Driver.getCurrentUrl());
            System.out.println("Navigated to correct webpage\n");
            System.out.println(base.Driver.getCurrentUrl());
        }
        catch(Throwable pageNavigationError){
            System.out.println("Incorrect webpage\n");
            Assert.fail();
        }


    }

    @And("^I want to upload a portfolio$")
    public void iWantToUploadAPortfolio() throws Throwable {

    }

    @And("^I want to valued a portfolio$")
    public void iWantToValuedAPortfolio() throws Throwable {
    }

    @And("^I want to generate a MarginCalls$")
    public void iWantToGenerateAMarginCalls() throws Throwable {
    }

    @Then("^I want to send MarginCalls$")
    public void iWantToSendMarginCalls() throws Throwable {
    }
}
