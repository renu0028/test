package renu.java.app;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import junit.framework.Assert;

public class AppTest extends TestCase {
public AppTest(String testName){
super(testName);
double result =App.calculateSimpleInterest(10000,5,7);
Assert.assertEquals("Test failed. ",35000.0,result);
}

public static Test suite(){
return new TestSuite(AppTest.class);
}
public void testApp(){
assertTrue(true);
}
}
