/*
Select a Complex Code Segment: 
Choose a complex code segment from your current projects, 
an open-source repository, or a past programming assignment. 
Open an issue on your team repository detailing the complexity 
and the challenges you’re facing in understanding the code.
*/


// The visitMethodDecl function checks method modifiers and performs type checking
void visitMethodDecl(MethodDecl *md) {
    // Check if the method is public or private
    if (md->isPublic() && md->isPrivate()) {
        reportError("A method cannot be both public and private.");
    }

    // Check if the method is static
    if (md->isStatic()) {
        if (md->getReturnType()->isPrimitive() && md->isFinal()) {
            // Static final methods cannot return primitive types
            reportError("Static final methods cannot return primitive types.");
        }
       
    }

   
    if (md->isAbstract() && md->isFinal()) {
        reportError("A method cannot be both abstract and final.");
    }

    for (auto &param : md->getParameters()) {
        if (!param->getType()->isValid()) {
            reportError("Parameter type is invalid in method: " + md->getName());
        }
    }


/*
Implement Changes: 
Apply ChatGPT’s recommendations to simplify or optimize 
the code, ensuring that functionality is maintained.
*/
// Helper function for error reporting with method context
void reportMethodError(const std::string& message, MethodDecl* md) {
    reportError(message + " Method: " + md->getName());
}

// Simplified and refactored version of visitMethodDecl
void visitMethodDecl(MethodDecl *md) {
    // Check if the method is both public and private
    if (md->isPublic() && md->isPrivate()) {
        reportMethodError("A method cannot be both public and private.", md);
    }

    // Check if the method is static and final, ensuring static final methods don't return primitive types
    if (md->isStatic() && md->isFinal()) {
        if (md->getReturnType()->isPrimitive()) {
            reportMethodError("Static final methods cannot return primitive types.", md);
        }
    }

    // Check if the method is both abstract and final
    if (md->isAbstract() && md->isFinal()) {
        reportMethodError("A method cannot be both abstract and final.", md);
    }

    // Validate parameter types
    for (auto &param : md->getParameters()) {
        if (!param->getType()->isValid()) {
            reportMethodError("Parameter type is invalid.", md);
        }
    }
}

// done