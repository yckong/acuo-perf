package Steps;

import Base.BaseUtil;
import cucumber.api.java.en.And;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebElement;
import org.testng.Assert;

import java.util.List;
import java.util.NoSuchElementException;
import java.util.concurrent.TimeUnit;

public class LoginStep extends BaseUtil {

    private BaseUtil base;

    public LoginStep(BaseUtil base) {
        this.base = base;
    }



    @Then("^I should see the dashboard$")
    public void iShouldSeeTheDashdashboard() throws Throwable {

        System.out.println("I should see the DashBoard\n");
        //Check URL loaded
        //Proceed if correct URL is loaded
        //Fail if incorrect URL is loaded
        String expectedUrl = "https://uat.acuo.com/#/dashboard";
        try{
            Assert.assertEquals(expectedUrl,base.Driver.getCurrentUrl());
            System.out.println("Navigated to correct webpage");
        }
        catch(Throwable pageNavigationError){
            System.out.println("Incorrect webpage\n");
            Assert.fail();
        }
    }

    @Given("^Navigate to login prompt$")
    public void navigateToLoginPrompt() throws Throwable {

        System.out.println("I should see the login prompt\n");
        //Navigate to login page
        base.Driver.get("http://uat.acuo.com/");
        //Proceed if URL is correct
        //Fail if the URL is incorrect
        String expectedUrl = "https://uat.acuo.com/#/";
        try{
            Assert.assertEquals(expectedUrl,base.Driver.getCurrentUrl());
            System.out.println("Navigated to correct webpage");
        }
        catch(Throwable pageNavigationError){
            System.out.println("Incorrect webpage\n");
            Assert.fail();
        }
    }

    @And("^I click login button$")
    public void iClickLoginButton() throws Throwable {

        System.out.println("I click on login button\n");
        WebElement element;
        element = base.Driver.findElement(By.xpath("//div[@class='Login__buttonHolder___3TWr4']"));
        element.click();

        //Check username and password.
        List<WebElement> foundElement = base.Driver.findElements(By.xpath("//div[@class='Login__pw_error___3qDZz']"));
        if (foundElement.size() > 0)
        {
            System.out.println("Incorrect username or password");
            Assert.fail();
        } else {
            System.out.println("Login Successful");
        }

        //Bypass 2FA by clicking enter
        //Check if 2FA prompt appear (Element check "2FA SECURITY CODE")
        base.Driver.findElement(By.xpath("//div[text()[contains(.,\'2FA SECURITY CODE\')]]"));
        base.Driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        element = base.Driver.findElement(By.xpath("//div[@class='TwoFA__buttonHolder___23naz']"));
        element.click();
    }

    @And("^I enter the username and password$")
    public void iEnterTheUsernameAsAndPasswordAs() throws Throwable {
        //Check if Login prompt appear (element check "sign in")
        base.Driver.findElement(By.xpath("//button[text()[contains(.,\'sign in\')]]"));

        //Define username and password
        String userName = "user@acuocpty.com";
        String passWord = "@Password1";
        System.out.println("username as " + userName);
        System.out.println("\npassword as " + passWord);

        //Enter username and password
        WebElement element;
        element = base.Driver.findElement(By.className("Login__input___3nbxz"));
        base.Driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
        element.sendKeys(Keys.chord(Keys.CONTROL, "a"));
        base.Driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
        //key in username
        element.sendKeys(userName);
        element.sendKeys(Keys.chord(Keys.TAB));
        element.sendKeys(Keys.chord(Keys.CONTROL, "a"));
        base.Driver.manage().timeouts().implicitlyWait(1, TimeUnit.SECONDS);
        //key in the password
        element.sendKeys(passWord);


    }

}
