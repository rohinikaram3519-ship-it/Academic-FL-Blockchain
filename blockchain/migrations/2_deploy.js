const AcademicVerification =
artifacts.require("AcademicVerification");

module.exports = function(deployer) {
    deployer.deploy(AcademicVerification);
};